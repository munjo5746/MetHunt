from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from Hunt.models import Hunt
from Hunt.models import Item

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
    data.update({'url' : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(-1)})

    return render_to_response(page, data)

@login_required(login_url="/UserAuthentication/LogIn")
def HuntDetail(request, HuntPk, CurrentIndex):
    """
    CurrentIndex : This index will be used for the index of the Hunt.Items
    to find the Item instance. So on the current page, the CurrentIndex passing
    into the next page will be the index of the item that will be displayed on
    the page with the HttpResponse.
    """

    # init variables
    HuntPk = int(HuntPk)
    CurrentIndex = int(CurrentIndex)

    data = {}
    page = None
    hunt = None
    items = None
    item = None
    try:
        hunt = Hunt.objects.get(pk=HuntPk)
        items = json.loads(hunt.Items)
    except:
        raise Http404

    # block if CurrentIndex is -1
    if CurrentIndex == -1:
        try:
            item = Item.objects.get(pk=items[CurrentIndex + 1]) # at 0 index
        except:
            raise Http404
        page = "HuntDetail.html"
        data.update({"user" : request.user})
        data.update({"Item" : item})
        data.update({"Title" : str(CurrentIndex + 1) + "th Question"})
        data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex + 1)})
        data.update({"error" : None})
        return render_to_response(page, data)

    # get the size of the item list
    listSize = len(items)
    if listSize - 1 == CurrentIndex:
        # we need to direct the user to congrat page for compeleting the Hunt.
        page = "congratPage"
        return render_to_response(page, data)

    # get the previous item.
    prevItem = Item.objects.get(pk=items[CurrentIndex])

    # get the submitted answer.
    Answer = request.GET.get("Answer")


    # compare the answer.
    if request.method == "GET" and Answer is not None:

        if str(Answer) == prevItem.QuestionId:
            # the user got the answer..
            print "The answer is right, answer : " + str(Answer)
            # The CurrentIndex is not the last one. That means there is more
            # items to populate. Also, at this moment, the answer is correct.
            # It means we need to populate next Item.

            # get the item
            item = Item.objects.get(pk=items[CurrentIndex + 1]) # the next item

            # set the data we need
            page = "HuntDetail.html"
            data.update({"user" : request.user})
            data.update({"Item" : item})
            data.update({"Title" : str(CurrentIndex + 1) + "th Question"})
            data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex + 1)})
            return render_to_response(page, data)
        else:
            # the submitted answer is wrong..
            # show that the submitted answer is wrong...
            page = "HuntDetail.html"
            data.update({"user" : request.user})
            data.update({"Title" : "Incorrect Answer"})
            data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex)})
            data.update({"error" : "The submmitted answer is not correct!"})
            print "The answer is wrong, answer : " + str(Answer)
            return render_to_response(page, data)





    return render_to_response(page, data)
