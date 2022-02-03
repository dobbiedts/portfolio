from django.shortcuts import render, redirect
from .models import *
from django.core.mail import  EmailMessage
from django.contrib import messages

# Create your views here.
def home(request):
    header = 'Welcome : This is the home page'
    
    context = {
        "header" : header,
    }
    return render(request, 'home.html', context)

def post(request):
    header = 'Welcome : This is the post page'
    
    context = {
        "header" : header,
    }
    return render(request, 'post.html', context)

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name',"")
        email= request.POST.get('email',"")
        subject= request.POST.get('subject',"")
        message= request.POST.get('message',"")
        
        
        msg= Message(name=name, email=email, subject=subject, message=message)
        
        msg.save()
        
        #to = request.POST['email_to']     
        recipient_list = ['olaoluwaakinloye@gmail.com']
        mail = EmailMessage(subject, message, from_email='', to=recipient_list)  
        if mail.send(fail_silently=False) :
            messages.success(request, 'Mail sent successfully')      
        return redirect('home')
