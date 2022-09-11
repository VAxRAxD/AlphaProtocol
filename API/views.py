import random, string, smtplib, datetime
from django.http import HttpResponse
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

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/regusr',
        'POST/ap/genotp/',
        'POST/ap/verotp/',
    ]
    return Response(routes)

def regUser(request):
    return render(request,'API/genotp.html')

@api_view(['POST'])
def genOtp(request):
    global stories,current
    if cache.get('otp'):
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    # otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}{stories[current]}"
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}2"
    if current<2:
        current+=1
    else:
        current=0
    cache.set('otp',otp,300)
    your_email = config.EMAIL
    your_password = config.PASSWORD
    sender=request.POST['mail']
    # establishing connection with gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    # the message to be emailed
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = sender
    msg['Subject'] = 'OTP for alpha protocol'
    # string to store the body of the mail
    body = f"{otp}"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(your_email, [sender], msg.as_string())
    server.close()
    LeaderBoard.objects.create(id=otp,email=sender)
    return render(request,'API/genotp.html')

@api_view(['POST'])
def verOtp(request):
    otp=cache.get('otp')
    code=request.data[0]['code']
    if otp==code:
        cache.delete('otp')
        story=otp[-1]
        data=[
            {
                'img': f'{config.PREFIX_URL}/Intro/Intro.jpg'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level1.png',
                'ans':f'APGSL1'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level2.png',
                'ans':f'VD{story}L2'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level3.png',
                'ans':f'AK{story}L3'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level4.png',
                'ans':f'LE{story}L4'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level5.png',
                'ans':f'AN{story}L5'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level6.png',
                'ans':f'AC{story}L6'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level7.png',
                'ans':f'CL{story}L7'
            },
            {
                'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level8.png',
                'ans':f'RT{story}L8'
            }
        ]
        return Response(data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addScore(request):
    otp=request.data[0]['otp']
    level=request.data[0]['level']
    minute=request.data[0]['minute']
    second=request.data[0]['second']
    grp=LeaderBoard.objects.get(id=otp)
    grp.level=level
    grp.time=datetime.time(0,minute,second)
    grp.save()
    return Response(status=status.HTTP_200_OK)