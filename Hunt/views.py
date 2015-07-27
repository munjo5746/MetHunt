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

    return render_to_response('HuntBegin.html', data)

@login_required(login_url="/UserAuthentication/LogIn")
def HuntDetail(request, HuntPk, CurrentIndex):
    
    data = {}
    page = "HuntBegin.html"
    print CurrentIndex, HuntPk
    return render_to_response(page, data)
