from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('regusr/',views.regUser,name="regUser"),
    path('genotp/',views.genOtp,name="genOtp"),
    path('verotp',views.verOtp,name="verOtp"),
    path('elmVerotp',views.elmVerOtp,name="elmVerOtp"),
    path('addscr',views.addScore,name="addScr"),
    path('getotp/<str:mail>',views.getOtp, name="getOtp"),
    path('ldrbrd/<str:day>',views.leaderBoard, name="ldrbrd"),
    path('delotp/<str:mail>',views.delOtp,name="delOtp"),
    path('regseat/',views.regSeat,name="regst"),
    path('getseat',views.getSeat,name="getst"),
    path('rstseat',views.resetSeat,name='regseat')
]