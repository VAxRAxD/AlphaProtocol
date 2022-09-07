import random, string, smtplib
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from AlphaProtocol import config

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/genotp/',
        'GET/ap/verotp/:otp',
        'GET/ap/getintro',
        'GET/ap/getimg/:story'
    ]
    return Response(routes)

def regUsr(request):
    return render(request,'API/genotp.html')

@api_view(['POST'])
def genOtp(request):
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}{random.randint(1,3)}"
    cache.set('otp',otp,120)

    
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
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def verOtp(request):
    otp=cache.get('otp')
    code=3
    if otp==code:
        cache.delete('otp')
        story=otp[-1]
        data=[
        {
            'img': f'{config.PREFIX_URL}/Intro/Intro.jpg'
        },
        {
            'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level1.png',
            'ans':f'Leve1'
        },
        {
            'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level2.png',
            'ans':f'Story{story}Level2'
        }
    ]
        return Response(data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getImg(request,story):
    data=[
        {
            'img': f'{config.PREFIX_URL}/Intro/Intro.jpg'
        },
        {
            'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level1.png',
            'ans':f'Leve1'
        },
        {
            'img':f'{config.PREFIX_URL}/StoryLine_{story}/Level2.png',
            'ans':f'Story{story}Level2'
        }
    ]
    return Response(data)

def getcode(request):
    otp=cache.get('otp')
    if otp:
        return HttpResponse(otp)
    else:
        return HttpResponse("Code expired")

def verusr(request):
    return render(request, 'API/verotp.html')

@api_view(['POST'])
def temp(request):
    content=request.data
    return HttpResponse(content[0]['data'])