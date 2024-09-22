from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home, name="home"),
    path('2D/',views.TwoD,name="2D"),
    path('3D/',views.ThreeD,name="3D"),
    path('Icon/',views.Icon,name="Icon"),
    path('About/',views.About,name="About"),
    path('Contact/',views.Contact,name="Contact"),
    path('collection/',views.collection, name="collection"),
    path('search/',views.search,name="search"),
    path('Signin/',views.Signin, name="Signin"),
    path('register/',views.register,name="register"),
    path('logout/',views.logoutuser, name="logout"),
    path('update_download/',views.updateDownload, name="update_download"),
]
