
from django.contrib import messages
from django.shortcuts import render, redirect,reverse
from datetime import datetime
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from services.service  import *
 
from ..form.user_form import  RegistrarFotos
from web import config 
from requests import get


#Redireccionar al inicio
def capture(request): 
    if request.method == 'POST' :
        form = RegistrarFotos(request.POST)
        if form.is_valid():       
            user = get_capture(form.cleaned_data['fullName'] )
    else:
        form = RegistrarFotos()
    return render(request, 'biometric/capture.html', {'form':form} )
