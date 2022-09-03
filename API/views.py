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
    cache.set('otp',otp,30)
    data=[otp]
    return Response(data)

@api_view(['POST'])
def verOtp(request,code):
    otp=cache.get('otp')
    if otp==code:
        cache.delete('otp')
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def getcode(request):
    otp=cache.get('otp')
    if otp:
        return HttpResponse(otp)
    else:
        return HttpResponse("Code expired")