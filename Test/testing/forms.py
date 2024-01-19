from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#converting django models to a form

from django.contrib.auth.models import User

#using forms class
from django import forms
#to use widget (fields)
from django.forms.widgets import PasswordInput,TextInput

#Json Extraction.
import json
import os


users = User.objects.all()

visual_data = {
    'name': 'Users',
     'children': []
}

for user in users:
    user_node = {
        'name': user.username,
        'children': [
            { 'name': user.email, 
              }
        ] 
    }
    
    visual_data['children'].append(user_node)

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)


target_dir = os.path.join("static","testing", "js") 


full_path = os.path.join(parent_dir, target_dir)


filename = "e65374209781891f37dea1e7a6e1c5e020a3009b8aedf113b4c80942018887a1176ad4945cf14444603ff91d3da371b3b0d72419fa8d2ee0f6e815732475d5de.json"

file_path = os.path.join(full_path, filename)

with open(file_path, 'w') as f:
   json.dump(visual_data, f)


#modifying the Existing default UserCreation Form

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields =['username','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use. Please use a different one.")
        return email


#modifying the existing User Authentication

class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    
    password=forms.CharField(widget=PasswordInput())

    