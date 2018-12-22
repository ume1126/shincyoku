from django.urls import path
from . import views

app_name = 'main' #django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.select_room, name='main'),
    path('create_room/', views.create_room, name='create_room'),

    path('room/<int:room_pk>/', views.room, name='room'),

    # path('create_shincyoku/', views.create_shincyoku, name='create_shincyoku'),
    path('create_shincyoku/<int:shincyoku_pk>/', views.create_shincyoku, name='create_shincyoku'),
    path('room/<int:room_pk>/shincyoku_delete/<int:shincyoku_pk>/', views.delete_shincyoku, name='delete_shincyoku'),
    path('shincyoku/<int:shincyoku_pk>/', views.shincyoku, name='shincyoku'),
    path('edit/<int:shincyoku_pk>/', views.edit_shincyoku, name='edit_shincyoku'),
    path('room/<int:room_pk>/delete/', views.delete_room, name='delete_room'),

    path('countup/<int:shincyoku_pk>/', views.countup, name='countup'),

    # path('test/', views.main, name='main'),

    # path('select_room/', views.select_room, name='select_room'),
    # path('create_room/', views.create_room, name='create_room'),
    # path('room/<int:pk>/', views.room, name='room'),

    # path('shincyoku/<int:pk>/', views.shincyoku, name='shincyoku'),
    # path('yaruzo/', views.create_shincyoku, name='create_shincyoku'),



]
