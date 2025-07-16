"""project1 URL Configuration

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
from user import  views as usr
from admin import views as admns
from ImageRecognition.views import index, adminlogin, UserLogin, UserRegisterAction, UserRegister
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('', index, name="index"),
    path('adminlogin/', adminlogin, name="adminlogin"),
    path('UserRegister/', UserRegister, name="UserRegister"),


    ### User Side Views
    path('UserLogin/', UserLogin, name='UserLogin'),
    path('UserLoginCheck/', usr.UserLoginCheck, name='UserLoginCheck'),
    path('UserRegisterAction/', UserRegisterAction, name='UserRegisterAction'),
    path('UserHome/', usr.UserHome, name="UserHome"),
    path('UserUploadImageForm/', usr.UserUploadImageForm, name="UserUploadImageForm"),
    path("UserImageProcessFirst/", usr.UserImageProcessFirst, name="UserImageProcessFirst"),
    path("UserImageAIForm/", usr.UserImageAIForm, name="UserImageAIForm"),
    path("ProcessUserImageAI/", usr.ProcessUserImageAI, name="ProcessUserImageAI"),
    path("StartTraining/", usr.StartTraining, name="StartTraining"),

    ### Admin Side Views
    path('adminhome/', admns.adminhome, name="adminhome"),
    path("AdminLoginCheck/", admns.AdminLoginCheck, name="AdminLoginCheck"),
    path('RegisterUsersView/', admns.RegisterUsersView, name='RegisterUsersView'),
    path('ActivaUsers/', admns.ActivaUsers, name='ActivaUsers'),
    path('AdminResults/', admns.AdminResults, name='AdminResults'),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
