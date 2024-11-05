from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'), #This line in urls.py is a dynamic route that matches any string following the base URL. When you redirect to /chatroom1, it matches this pattern, and Django knows to invoke the room view function for that URL. So the room view will handle the request, even though it’s not explicitly listed.
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]