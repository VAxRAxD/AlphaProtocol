from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('genotp/<str:phone>',views.genOtp,name="genOtp"),
    path('verotp/<str:code>/',views.verOtp,name="verOtp"),
    path('getotp',views.getcode,name="code"),
    path('getintro',views.getIntro,name="getIntro"),
    path('getimg/<str:story>/',views.getImg,name="getImg"),
]