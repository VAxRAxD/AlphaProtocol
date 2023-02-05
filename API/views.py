import random, string, smtplib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from AlphaProtocol import config
from . models import *

stories=[1,2,3]
current=0
day=1

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/regusr/',
        'POST/ap/genotp/',
        'POST/ap/verotp/',
        'GET/ap/getotp/',
        'GET/ap/delotp/',
        'POST/ap/addscr/',
        'GET/ap/ldrbrd/'
    ]
    return Response(routes)

@api_view(['GET'])
def regUser(request,mail):
    try :
        LeaderBoard.objects.get(email=mail)
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    except: pass
    return render(request,'API/genotp.html')

@api_view(['POST'])
def genOtp(request):
    mail=request.POST['mail']
    username=request.POST['username']
    global stories,current,day
    if cache.get(mail):
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}D{day}S{stories[current]}"
    if current<2:
        current+=1
    else:
        current=0
    cache.set(mail,otp,300)
    your_email = config.EMAIL
    your_password = config.PASSWORD
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = mail
    msg['Subject'] = 'OTP for alpha protocol'
    body = f"{otp}"
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(your_email, [mail], msg.as_string())
    server.close()
    LeaderBoard.objects.create(story=otp[-1],name=username,email=mail)
    return render(request,'API/genotp.html')

@api_view(['POST'])
def verOtp(request):
    code=request.data[0]['otp']
    mail=request.data[0]['email']
    otp=cache.get(mail)
    print(otp)
    if otp==code:
        cache.delete(mail)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addScore(request):
    email=request.data[0]['email']
    level=request.data[0]['level']
    time=request.data[0]['time']
    grp=LeaderBoard.objects.get(email=email)
    grp.level=level
    grp.completion=time
    grp.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getOtp(request,mail):
    data=[
        {
            "code":cache.get(mail)
        }
    ]
    return Response(data)

def leaderBoard(request):
    data=LeaderBoard.objects.all().exclude(level__isnull=True).order_by('-level','completion')[:10]
    context={
        "data":data
    }
    return render(request,'API/leaderboard.html',context)

@api_view(['GET'])
def delOtp(request,mail):
    global current
    if cache.get(mail):
        cache.delete(mail)
        current-=1
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)