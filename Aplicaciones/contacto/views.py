from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models import Contacto

def contacto(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()
        #return HttpResponse("El registro fue ingresado")
        #email(obj_contact)

        return render(request,"pages/gracias.html",)
    return render(request,"pages/contacto.html",)
def email(email):
    subject = 'Thank you for contact me'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['santiagoescarpetaramirez@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return True
    
