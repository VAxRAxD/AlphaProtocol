from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('regusr',views.regUsr,name="regUser"),
    path('genotp',views.genOtp,name="genOtp"),
    path('verotp',views.verOtp,name="verOtp"),
    path('getotp',views.getcode,name="code"),
    path('getimg/<str:story>',views.getImg,name="getImg"),
    path('test',views.temp, name="testing"),
    path('verusr',views.verusr, name="verUSer"),

]