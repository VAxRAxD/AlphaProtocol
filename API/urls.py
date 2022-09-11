from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('lddata',views.loadData,name="loadData"),
    path('regusr',views.regUser,name="regUser"),
    path('genotp',views.genOtp,name="genOtp"),
    path('verotp',views.verOtp,name="verOtp"),
    path('addscr',views.addScore,name="addScr"),
    path('vwche/<str:id>', views.viewCache,name="viewCache")
]