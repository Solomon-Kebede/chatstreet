from django.urls import path
from . import views



urlpatterns = [
	path('index/', views.index, name="index"),
	path('chatroom/', views.chatRoom, name="chatroom"),
	# path("<str:room_name>/", views.chatRoom, name="chatroom"),

]
