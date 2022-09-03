import random, string
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/genotp',
        'GET/ap/verotp/:otp'
    ]
    return Response(routes)

@api_view(['GET'])
def genOtp(request):
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}{random.randint(1,3)}"
    cache.set('otp',otp,120)
    data=[otp]
    return Response(data)

@api_view(['GET'])
def verOtp(request,code):
    otp=cache.get('otp')
    if otp==code:
        cache.delete('otp')
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getImg(request):
    data=[
        'https://res.cloudinary.com/docvlyucw/image/upload/v1662212883/Alpha%20Protocol/StoryLine_1/Intro.png',
        'https://res.cloudinary.com/docvlyucw/image/upload/v1662212887/Alpha%20Protocol/StoryLine_1/Story1Level1.png',
        'https://res.cloudinary.com/docvlyucw/image/upload/v1662212890/Alpha%20Protocol/StoryLine_1/Story1Level2.png',
    ]
    return Response(data)

def getcode(request):
    otp=cache.get('otp')
    if otp:
        return HttpResponse(otp)
    else:
        return HttpResponse("Code expired")