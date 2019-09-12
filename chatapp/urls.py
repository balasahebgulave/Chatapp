from django.urls import path, include
from . views import chat, issue, trainbot, login_user, logout_user
from django.contrib.auth import views


urlpatterns = [
    path('',chat, name='chat'),
    path('issue',issue, name='issue'),
    path('trainbot',trainbot, name='trainbot'),
    path('login/',login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
