from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('regusr/',views.regUser,name="regUser"),
    path('genotp/',views.genOtp,name="genOtp"),
    path('verotp',views.verOtp,name="verOtp"),
    path('addscr',views.addScore,name="addScr"),
    path('getotp/<str:mail>',views.getOtp, name="getOtp"),
    path('ldrbrd',views.leaderBoard,name="leaderBoard"),
    path('delotp/<str:mail>',views.delOtp,name="delOtp")
]