from UserAuthentication.models import UserModel
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


class UserSerializer(serializers.ModelSerializer):

    def SaveUser(self, request):
        if self.data == None:
            return

        username = self.data['UserName']
        password = self.data['Password']
        firstname = self.data['FirstName']
        lastname = self.data['LastName']
        email = self.data['Email']

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
            if user is not None:
                login(request, user)
            return True


    class Meta:
        model = UserModel
        fields = ('UserName','Password', 'Email', 'FirstName', 'LastName')

class LogInSerializer(serializers.ModelSerializer):

    def UserLogIn(self, request):
        if self.data is None:
            print "self.data in UserLogIn is None"
            return
        username = self.data['UserName']
        password = self.data['Password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        return False




    class Meta:
        model = UserModel
        fields = ('UserName', 'Password')
