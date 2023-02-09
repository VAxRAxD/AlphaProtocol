import random, string, smtplib,requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from django.views.decorators.csrf import csrf_exempt
from email.mime.text import MIMEText
from AlphaProtocol import config
from . models import *

levels=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
day=3
grps=0

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET/ap/regusr/',
        'POST/ap/genotp/',
        'POST/ap/verotp/',
        'POST/ap/elmVerotp/',
        'GET/ap/getotp/<email>/',
        'GET/ap/delotp/<email>/',
        'POST/ap/addscr/',
        'GET/ap/ldrbrd/<story>/',
        'GET/ap/getplrs/<day>/<story>/',
        'GET/ap/iniotp/',
        'GET/ap/regseat/',
        "GET/ap/getseat/"
    ]
    return Response(routes)

@api_view(['GET'])
def regUser(request):
    return render(request,'API/genotp.html')

def genOtp(request):
    global day,grps
    mail=request.POST.get('mail',False)
    username=request.POST.get('username',False)
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': mail})
    status = response.json()['status']
    if status == "valid":
        pass
    else:
        return render(request,'API/email.html')
    if cache.get(mail):
        return render(request,'API/check.html')
    otp=f"{random.randint(10,99)}{random.choice(string.ascii_letters)}D{day}{levels[grps]}"
    grps+=1
    cache.set(mail,otp,None)
    your_email = config.EMAIL
    your_password = config.PASSWORD
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = mail
    msg['Subject'] = 'OTP for alpha protocol'
    body = f"Thank you for registering for treasure hunt . Your one time password to get started is {otp}.We hope you keep it confidential. Vamos!!"
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(your_email, [mail], msg.as_string())
    server.close()
    LeaderBoard.objects.create(story=otp[-1],name=username,email=mail,day=2)
    return render(request,'API/success.html')

@api_view(['POST'])
def verOtp(request):
    code=request.data[0]['otp']
    mail=request.data[0]['email']
    otp=cache.get(mail)
    if otp==code:
        cache.delete(mail)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def elmVerOtp(request):
    code=request.data[0]['otp']
    mail=request.data[0]['email']
    otp=cache.get(mail)
    if otp==code:
        # cache.delete(mail)
        indx=int(otp[-2::])
        combinations=list()
        for i in range(len(levels)):
            data=list()
            j=i
            count=0
            while count<len(levels):
                if j>=len(levels):
                    j=0
                data.append({ "img": f"https://res.cloudinary.com/docvlyucw/image/upload/v1675605007/Iris%202023/Day%203/{levels[j]}.png" })
                j+=1
                count+=1
            combinations.append(data)
        return Response(combinations[indx-1])
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

def leaderBoard(request,day):
    data=LeaderBoard.objects.filter(day=day).exclude(level__isnull=True).order_by('-level','completion')
    context={
        "data":data
    }
    return render(request,'API/leaderboard.html',context)

@api_view(['GET'])
def delOtp(request,mail):
    if cache.get(mail):
        cache.delete(mail)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)

def getplayers(request,day,story):
    data=LeaderBoard.objects.filter(story=story,day=day).exclude(level__isnull=True).order_by('-level','completion')
    context={
        "data":data
    }
    return render(request,'API/leaderboard.html',context)

@api_view(['GET'])
def regSeat(request):
    if cache.get('seat'):
        cache.set('seat',cache.get('seat')+1,None)
    else:
        cache.set('seat',1,None)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getSeat(request):
    data=[
        {
            "seat":cache.get('seat')
        }
    ]
    return Response(data)