
from django.contrib import messages
from django.shortcuts import render, redirect,reverse
from datetime import datetime
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from services.service  import *
 
from ..form.user_form import  RegisterForm
from web import config 
from requests import get


 

#Redireccionar al inicio
def welcome(request): 
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():       
            since=form.cleaned_data['since']

            date_object = datetime.strptime(since, '%d/%m/%Y')

            fecha_str = datetime.strftime(date_object, '%Y/%m/%d')
            user = post_send_email_verify(getClientIp(request),form.cleaned_data['fullName'] ,fecha_str ,form.cleaned_data['weeks'] ,
                                    form.cleaned_data['adult'] , form.cleaned_data['children'] ,
                                     form.cleaned_data['email'] )        
            if user['success'] == True:    
                  messages.success(request, "Correo enviado")
            else: 
                 messages.error(request,"No se puedo enviar correo")
            return  HttpResponseRedirect(reverse('welcome'))
    else:
        form = RegisterForm()
    return render(request, 'web_site/main.html', {'form':form} )



#Redireccionar a about
def about(request): 
    return render(request, 'web_site/about.html')



#Redireccionar a contact
def contact(request):     
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():       
            user = post_send_email_verify(form.cleaned_data['fullName'] ,form.cleaned_data['since'] ,form.cleaned_data['weeks'] ,
                                    form.cleaned_data['adult'] , form.cleaned_data['cboprofile'] , form.cleaned_data['children'] ,
                                    form.cleaned_data['email'] )        
            if user['success'] == True:    
                  messages.success(request, "Correo Enviado")
            else: 
                 messages.error(request,"No se puedo enviar correo")
            return  HttpResponseRedirect(reverse('welcome'))
    else:
        form = RegisterForm()
    return render(request, 'web_site/contact.html', {'form':form})

#Redireccionar a rooms
def rooms(request): 
    return render(request, 'web_site/rooms.html')

#Redireccionar a services
def services(request): 
    return render(request, 'web_site/services.html')

#Controlador para solicitar la recuperación de la password
def recover_password(request):
    if 'user_id' in request.session:
        return welcome(request)  
    if request.method == 'POST':
        form = RecoverPassword(request.POST)
        if form.is_valid():
            email = post_recover_password(form.cleaned_data['email'] ,getClientIp(request))
            if email['success']:          
                messages.success(request, EMAIL_SEND())
                return  HttpResponseRedirect(reverse('login'))
            else:
                messages.success(request, email['messages'])
                form.cleaned_data['email']  = ""
                return   HttpResponseRedirect(reverse('login'))
    else:
        form = RecoverPassword()
    return render(request, 'auth/recover.html',{'form':form})

def getClientIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip