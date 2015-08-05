from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def HomeMain(request):

    # init
    data = {'error' : None, 'user' : None}

    if request.user.is_authenticated:
        data['user'] = request.user

    return render_to_response('Home.html', data)
    # return HttpResponse("Hello")

def About(request):
    page = "About.html"
    data = {}

    return render_to_response(page, data)
