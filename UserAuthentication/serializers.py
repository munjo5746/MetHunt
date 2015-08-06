from UserAuthentication.models import UserModel
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

class UserSerializer(serializers.ModelSerializer):

    def SaveUser(self, request):
        if self.data == None:
            return

        username = self.data['username']
        password = self.data['password']
        firstname = self.data['first_name']
        lastname = self.data['last_name']
        email = self.data['email']

        try:
            user = User.objects.create_user(
                    username = username,
                    password = password,
                    first_name = firstname,
                    last_name = lastname,
                    email = email)
        except:
            print username + " : Already exists."
            return False

        if user is not None:
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            # make UserModel
            userModel = UserModel(BelongTo = user)
            userModel.save()

            return True

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class LogInSerializer(serializers.ModelSerializer):

    def UserLogIn(self, request):
        if self.data is None:
            print "self.data in UserLogIn is None"
            return
        username = self.data['username']
        password = self.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        return False

    class Meta:
        model = User
        fields = ('username', 'password')
