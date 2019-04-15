from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import os
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
#import msal
from django.views.decorators.csrf import csrf_exempt
import jwt
from ValidateJWT.validatejwt import * 
#from msal.application import ClientApplication

this_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(this_dir, 'msal_config.JSON')
config  = json.load(open(config_file))


def authorize(request):
    # Create a preferably long-lived app instance which maintains a token cache.
    #app = msal.ConfidentialClientApplication(config["client_id"], authority=config["authority"],
    #client_credential=config["secret"])
    result = None
    #accounts = app.get_accounts(username=config["username"])
    #if accounts:
     #   print("Account(s) exists in cache, probably with token too. Let's try.")
      #  result = app.acquire_token_silent(config["scope"], account=accounts[0])

    if not result:
        print("No suitable token exists in cache. Let's get a new one from AAD.")
        authorization_url  = "'
        
    return HttpResponseRedirect(authorization_url)

@csrf_exempt
def callback_signin(request):
    #msal.application.ConfidentialClientApplication.acquire_token_by_authorization_code(code, scopes, redirect_uri)
    if(request.POST.get('id_token') is None):
        print('None')
        
    id_token = request.POST.get('id_token')
    code = request.POST.get("code")
    content = jwt.decode(id_token, verify=False)
    request.session['code'] = code
    request.session['id_token'] = id_token
    request.session['user_info'] = content['name']
    #res = requests.get("https://www.bbc.com")
    
    user_email = content['name']
    print(user_email)
    return render(request, "home.html", {'user_email':user_email,'id_token': id_token})

def home(request, user_email , id_token):
    return render(request, "home.html", {'user_email':user_email,'id_token': id_token})
    

@csrf_exempt
def verify_accesstoken(request):
    id_token = request.GET.get('id_token')
    content = jwt.decode(id_token, verify=False)
    request.session['id_token'] = id_token
    request.session['user_email'] = content['emails']
    user_email = content['emails']
    print(user_email)
    return render(request, "home.html", {'user_email':user_email,'id_token': id_token})

def getaccesstoken(request):
    print(request)
    
    acc_tok_url = ""
    acc_tok_b = requests.post(acc_tok_url)
    access_token_str = acc_tok_b.content.decode()
    acc_tok_dict = json.loads(access_token_str)
    access_token = acc_tok_dict['access_token']
    validate_jwt(access_token)
    user_email = request.session._session['user_info']
    return render(request, "home.html", {'user_email': user_email, 'access_token':access_token})

def logout1(request):    
    return HttpResponseRedirect("")

def resetpassword(request):    
    return HttpResponseRedirect("")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
