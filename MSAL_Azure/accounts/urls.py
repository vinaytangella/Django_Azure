from django.urls import path, re_path

from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
        path('signup/', views.SignUp.as_view(), name='signup'),
    path('authorize/', views.authorize, name="authorize"),
    path('callback_signin/', views.callback_signin, name = "callback"),
    path('verify_accesstoken/', views.verify_accesstoken, name = "verify_accesstoken"),
    path('getaccesstoken/', views.getaccesstoken, name = "getaccesstoken"),    
    path('logout1/', views.logout1, name = "logout"), 
    path('resetpassword/', views.resetpassword, name = "resetpassword"),    
]
