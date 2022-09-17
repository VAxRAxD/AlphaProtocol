from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('regusr',views.regUser,name="regUser"),
    path('genotp',views.genOtp,name="genOtp"),
    path('verotp',views.verOtp,name="verOtp"),
    path('addscr',views.addScore,name="addScr"),
    path('getotp',views.getOtp, name="getOtp"),
    path('ldrbrd',views.leaderBoard,name="leaderBoard"),
    path('delotp',views.delOtp,name="delOtp")
]