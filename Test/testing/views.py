from django.shortcuts import render,redirect

from . forms import CreateUserForm,LoginForm

#using the default django authentication model
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

#request is  is an HttpRequest object that contains information about the current request
def homepage(request):

    return render(request,'testing/index.html')
   #allow us to have a view of the homepage



def register(request):

    #post request
    form = CreateUserForm()
    #functionality to register the user
    if request.method =="POST" :
         #post it to the database
        form = CreateUserForm(request.POST)

        if form.is_valid():
           #saves to the database
            form.save()

            return redirect("my-login")


    # render it to the register 
    context ={'registerform' : form}
    return render(request,'testing/register.html',context)


def my_login(request):

     form = LoginForm()

     if request.method =="POST":

        form = LoginForm(request,data=request.POST)

        if form.is_valid():
            #Retrieving the data
            username = request.POST.get('username')
            password = request.POST.get('password')


            #Now we need to check the Username and Password

            user = authenticate(request, username=username ,password=password)

            if user is not None:

                auth.login(request, user)

                return  redirect("dashboard")

     context = {'loginform':form}

     return render(request,'testing/my-login.html',context)


@login_required(login_url ="my-login")
def dashboard(request):

    return render(request,'testing/dashboard.html')

@login_required(login_url ="my-login")
def visual(request):

    return render(request,'testing/visual.html')



def user_logout(request):

    auth.logout(request)

    return redirect("")