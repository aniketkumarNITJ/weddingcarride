from django.shortcuts import render, HttpResponse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
# Create your views here.

SENDER="admin@weddingcarride.com"
RECEIVER="ggrewal2014@gmail.com"
USERNAME="admin@weddingcarride.com"
PASSWORD="weddingcarride#12345"

def gallery(request):
    context = {
        "title": "ContactUs-WeddingCarRide"
    }

    if request.method=="GET":
        return render(request, "contactus/home.html", context=context)

    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    mesg = request.POST.get("msg")

    msg = MIMEMultipart()
    msg.set_unixfrom('author')
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg['Subject'] = 'Regarding The CarWeddingRide'
    message = f'Name: {name}\nPhone No: {phone}\nemail: {email}\nMessage: {mesg}'
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    mailserver.ehlo()
    mailserver.login(USERNAME, PASSWORD)
    mailserver.sendmail(SENDER,RECEIVER,msg.as_string())
    mailserver.quit()

    return render(request, "contactus/home.html", context=context)