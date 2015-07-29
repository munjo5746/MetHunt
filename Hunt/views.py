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
    in the Museum.
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
    CurrentIndex : This index will be used for the index of the Hunt.Items
    to find the Item instance. So on the current page, the CurrentIndex passing
    into the next page will be the index of the item that will be displayed on
    the page with the HttpResponse.
    """

    # init variables
    HuntPk = int(HuntPk)
    CurrentIndex = int(CurrentIndex)

    data = {}
    page = "HuntDetail.html"
    hunt = None
    item = None
    try:
        hunt = Hunt.objects.get(pk=HuntPk)
        items = json.loads(hunt.Items)
    except:
        raise Http404

    # get the size of the item list
    listSize = len(items)
    if listSize - 1 == CurrentIndex:
        # we need to direct the user to congrat page for compeleting the Hunt.
        page = "congratPage"
        return render_to_response(page, data)

    # get the previous item.
    prevItem = Item.objects.get(pk=items[CurrentIndex])

    # compare the answer.
    if request.method == "GET":
        Answer = request.GET.get("Answer")
        print Answer
        if Answer == prevItem.QuestionId:
            # the user got the answer..
            print "The answer is right, answer : " + str(Answer)
            return render_to_response("HuntBegin.html", {})
        else:
            # the submitted answer is wrong..
            print "The answer is wrong, answer : " + str(Answer)
            return render_to_response("HuntBegin.html", {})
    else:
        print "It is not get method!"
        return render_to_response("HuntBegin.html", {})

    # get the item
    item = Item.objects.get(pk=items[CurrentIndex + 1]) # the next item
    data.update({"Item" : item})
    data.update({"Title" : str(CurrentIndex + 1) + "th Question"})
    data.update({"url" : "/Hunt/HuntDetail/" + str(HuntPk) + "/" + str(CurrentIndex + 1)})

    return render_to_response(page, data)
