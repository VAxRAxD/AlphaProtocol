from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getroutes"),
    path('genotp',views.genOtp,name="genOtp"),
    path('verotp/<str:code>/',views.verOtp,name="verOtp"),
    path('getotp',views.getcode,name="code"),
    path('getimg',views.getImg,name="getImg"),
]