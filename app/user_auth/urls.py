import django.contrib.auth.views
from django.urls import path, include
from . import views

app_name='user_auth'

urlpatterns=[
    path('top/',views.top_page, name="top"), # リダイレクト
    path('login/', # ログイン
         django.contrib.auth.views.login,
         {
             'template_name': 'user_auth/login.html',
         },
         name='login'),
    path('logout/', # ログアウト
         django.contrib.auth.views.logout,
         {
             'template_name': 'user_auth/logout.html',
         },
         name='logout'),
]
