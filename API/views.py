import random, string, smtplib
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/genotp/',
        'GET/ap/verotp/:otp',
        'GET/ap/getintro',
        'GET/ap/getimg/:story'
    ]
    return Response(routes)

@api_view(['GET'])
def genOtp(request,phone):
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}{random.randint(1,3)}"
    cache.set('otp',otp,120)
    CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com"
    }
    EMAIL = "mastermindwebservice@gmail.com"
    PASSWORD = "wearemastermindwebdevelopers763"
    recipient = phone
    auth = (EMAIL, PASSWORD)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, otp)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def verOtp(request,code):
    otp=cache.get('otp')
    if otp==code:
        cache.delete('otp')
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getImg(request,story):
    data=[
        {
            'img': 'https://res.cloudinary.com/docvlyucw/image/upload/v1662390258/Alpha%20Protocol/Intro/Intro.jpg'
        },
        {
            'img':f'https://res.cloudinary.com/docvlyucw/image/upload/v1662212887/Alpha%20Protocol/StoryLine_{story}/Level1.png',
            'ans':f'Story{story}Leve1'
        },
        {
            'img':f'https://res.cloudinary.com/docvlyucw/image/upload/v1662212890/Alpha%20Protocol/StoryLine_{story}/Level2.png',
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