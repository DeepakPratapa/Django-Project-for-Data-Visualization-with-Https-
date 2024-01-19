from django.urls import path

from .import views
#import the views
urlpatterns = [

     path('',views.homepage,name=""),

    #name parameter helps us to switch over when using links , refering to particular route
     path('register',views.register,name="register"),
 
     #We can access the url by mentioning the path
     path('my-login',views.my_login,name="my-login"),
     
     path('dashboard',views.dashboard,name="dashboard"),

     path('visual',views.visual,name="visual"),

     path('user-logout',views.user_logout,name="user-logout"),
    
]
