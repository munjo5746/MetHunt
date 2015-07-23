from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from UserAuthentication import forms
from django.core.context_processors import csrf
from rest_framework.decorators import api_view
from UserAuthentication.serializers import UserSerializer
from UserAuthentication.serializers import LogInSerializer
from UserAuthentication.models import UserModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.
@api_view(['GET', 'POST'])
def SignUp(request):

    # init
    form = None
    data = {'error': None}
    page = "SignUpPage.html"

    # add csrf token
    data.update(csrf(request))

    if request.method == "POST":
        # received data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # if valid, save the User
            saved = serializer.SaveUser(request)
            if not saved:
                data['error'] = "User Already Exists."
                return render_to_response(page, data)
            # redirect to Home
            return redirect('/')
    else:
        form = forms.SignUpForm()
        data.update({"form" : form})

    return render_to_response(page, data)

@api_view(['GET', 'POST'])
def LogIn(request):

    # init
    form = None
    data = {'error' : None, 'user' : None}
    page = "LogInPage.html"
    data.update(csrf(request))

    if request.method == "POST":
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            IsAuthenticated = serializer.UserLogIn(request)
            if not IsAuthenticated:
                # case where the user is not validated.
                data['error'] = 'UserName does not exist or Password is not correct.'
                return render_to_response(page, data)
            data.update({'user' : request.user})
            return render_to_response("Home.html", data)
    else:
        form = forms.LoginForm()
        data.update({"form" : form})
    return render_to_response(page, data)


@api_view(['GET', 'POST'])
def Profile(request):

    # init
    data = {'error' : None}
    page = "ProfilePage.html"

    return render_to_response(page, data)


@login_required(login_url="/UserAuthentication/LogIn")
def Logout(request):
    data = {'error' : None, 'user' : None}
    logout(request)
    data['user'] = request.user
    page = "Home.html"

    return render_to_response(page, data)
