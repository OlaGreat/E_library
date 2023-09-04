from django.core.mail import send_mail, send_mass_mail, EmailMessage, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


# Create your views here.

def playground(request):
    try:
        message = BaseEmailMessage(
            templated_name='email/email.html',
            context={'name': 'Asa'}
        )
        message.send(['ola@gmail.com'])

        # 1
        # message = "this mail is sent from django"
        # mail = EmailMessage("Welcome mail", message,
        #                     "support@library.com",
        #                     ['cashmoney@gmail.com']
        #                     )
        # mail.attach_file('playground\\static\\images\\jerry.jpg')
        # mail.send()
        # 1


    except BadHeaderError:
        pass
    return HttpResponse("This be playground")


def welcome(request):
    return render(request, 'playground/welcome.html')
