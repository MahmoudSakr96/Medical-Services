"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import method1,login,forhospital,about,contact,Services,home,signup,signup2,userlogin,userdata,\
    hospitaldata,hospitallogin,contactdata,hospitaldata2,filter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', method1),
    path('home', home),
    path('login',login),
    path('forhospital',forhospital),
    path('about',about),
    path('Services',Services),
    path('contact',contact),
    path('signup',signup),
    path('signup2',signup2),
    path('userlogin',userlogin),
    path('userdata',userdata),
    path('hospitaldata',hospitaldata),
    path('hospitallogin',hospitallogin),
    path('contactdata',contactdata),
    path('hospitaldata2',hospitaldata2),
    path('filter', filter),




]
