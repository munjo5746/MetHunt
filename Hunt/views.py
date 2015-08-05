from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from Hunt.models import Hunt
from Hunt.models import Item
from UserAuthentication.models import UserModel
from django.contrib.auth.models import User

from Hunt.serializers import HuntBeginSerializer
# util libraries
import json

# Create your views here.
def Main(request):
    data = {}
    return render_to_response('HuntMain.html', data)

@login_required(login_url="/UserAuthentication/LogIn")
def HuntBegin(request, HuntPk):
    """
    This function will be called when the user clicks the Hunt they want to
    try out, and they will see the first Hunt page with starting Location
    in the Museum. At the beginning, the url arguments will be pass with
    HuntPk and -1 where the -1 indicate that it has been just started.
    """
    data = {}
    page = "HuntBegin.html"

    # first get the corresponding Hunt
    hunt = None
    try:
        hunt = Hunt.objects.get(pk=HuntPk)
    except:
        # cannot find the Hunt. Return 404 status code.
        raise Http404

    # get the list of items that are belong to this Hunt
    ListOfItems = json.loads(hunt.Items)
    serialized = HuntBeginSerializer(hunt)
    print serialized
    data.update({'Hunt' : serialized.data})
    data.update({'CurrentIndex' : 0})
    data.update({'url' : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(0)})

    return render_to_response(page, data)

@login_required(login_url="/UserAuthentication/LogIn")
def HuntDetail(request, HuntPk, CurrentIndex):
    """
    CurrentIndex : This index will be the index of the Hunt.Items for next
    question. So the passing url must contain the HuntPk and the CurrentIndex + 1.
    """

    # init variables
    HuntPk = int(HuntPk)
    CurrentIndex = int(CurrentIndex)

    # init variables
    data = {}
    page = "HuntDetail.html"
    hunt = None
    items = None
    item = None

    # handle the case when the answer is submitted.
    try:
        # get the GET argument.
        Answer = request.GET.get("Answer")
        print "Answer : ", Answer
    except Exception as e:
        print e

    if Answer is not None and len(Answer) != 0:
        print "Answer is not None and size != 0"
        # check if the answer is correct.
        # The CurrentIndex will be always greater than 0.
        # reset the CurrentIndex.
        CurrentIndex = CurrentIndex - 1
        try:
            hunt = Hunt.objects.get(pk=HuntPk)
            items = json.loads(hunt.Items)
            item = Item.objects.get(pk=items[CurrentIndex])
        except Exception as e:
            print e

        # check the answer.
        if Answer == item.QuestionId:
            print "Answer : ", Answer, "QuestionId : ", item.QuestionId

            # reset the CurrentIndex
            CurrentIndex = CurrentIndex + 1

            # redirect to the HuntCorrect page
            return redirect("/Hunt/HuntCorrect/" + str(HuntPk) + "/" + str(CurrentIndex))
        else:
            print "Answer : ", Answer, "Which is incorrect!"
            # answer is wrong
            data.update({"user" : request.user})
            data.update({"Items" : SetupItemStatus(items, CurrentIndex)})
            data.update({"Title" : "The answer is incorrect!"})
            data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex)})
            data.update({"error" : "Incorrect answer is submitted!"})
            return render_to_response(page, data)

    # get hunt, items, item
    try:
        hunt = Hunt.objects.get(pk=HuntPk)
        items = json.loads(hunt.Items)
        item = Item.objects.get(pk=items[CurrentIndex])
    except Exception as e:
        print e
        return Http404

    data.update({"Item" : item})
    data.update({"Items" : SetupItemStatus(items, CurrentIndex)})
    data.update({"Title" : str(CurrentIndex + 1) + "th Question"})
    data.update({"user" : request.user})
    data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex + 1)})
    data.update({"error" : None})
    return render_to_response(page, data)



@login_required(login_url="/UserAuthentication/LogIn")
def HuntCorrect(request, HuntPk, CurrentIndex):
    """
    The arguments CurrentIndex is the index of the next item. The reason is
    because the url we are passing to the html page is for the next item and
    this view function is called when the user submitted the correct answer and
    HuntDetail view function redirects to this view function. In the Correct page,
    we need to show the fact of the previous item and the url we are passing should
    be the CurrentIndex.
    """
    HuntPk = int(HuntPk)
    CurrentIndex = int(CurrentIndex)

    page = "HuntDetail.html"
    hunt = None
    items = None
    item = None
    data = {}
    print "Redirected"

    # check if the CurrentIndex > the last items index.
    # CurrentIndex != the last items index because if the user passed the
    # last question, the url contains CurrentIndex + 1 where the CurrentIndex
    # is greater than the last index.

    # get hunt and item.
    try:
        hunt = Hunt.objects.get(pk=HuntPk)
        items = json.loads(hunt.Items)
        item = Item.objects.get(pk=items[CurrentIndex - 1])
    except Exception as e:
        raise Http404

    if CurrentIndex > len(items) - 1:
        # the last item is finished.
        # redirect to the congrat page.
        print "Last item is finished!"
        page = "HuntCorrect.html"
        data.update({"user" : request.user})
        data.update({"Items" : SetupItemStatus(items, CurrentIndex)})
        data.update({"Item" : item})
        data.update({"Title" : "Fact"})
        data.update({"url" : "/Hunt/HuntCongrat/" + str(HuntPk)})
        data.update({"error" : None})
        return render_to_response(page, data)

    # set the data we need
    page = "HuntCorrect.html"
    data.update({"user" : request.user})
    data.update({"Item" : item})
    data.update({"Items" : SetupItemStatus(items, CurrentIndex - 1)})
    data.update({"Title" : "Fact"})
    data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex)})
    data.update({"error" : None})
    return render_to_response(page, data)

@login_required(login_url="/UserAuthentication/LogIn")
def HuntCongrat(request, HuntPk):
    """
    At this point, the user is completed the selected hunt. So we need to record
    it into the UserModel.
    """
    # init variables
    page = "HuntCongrat.html"
    user = User.objects.get(pk=request.user.pk) # the user must be exist


    return render_to_response(page, {})


@login_required(login_url="/UserAuthentication/LogIn")
def HuntCancel(request):
    """
    This view function is responsible for the case when the user clicks the
    cancel button on the top-right corner of the Hunt page. This will return the
    user to the HuntMain page.
    """

    # init variables
    page = "HuntMain.html"
    data = {}

    # set the data
    data.update({"error" : None})
    data.update({"user" : request.user})
    return render_to_response(page, data)

def SetupItemStatus(items, CurrentIndex):
    if len(items) == 0:
        return None

    result = []
    for index in xrange(len(items)):
        if index == CurrentIndex:
            result += [(index + 1, "active")]
        elif index < CurrentIndex:
            result += [(index + 1, "ProgressComplete")]
        else:
            result += [(index + 1, "disabled")]
    print "result : ", result
    return result
