from django.urls import path
from . import views 

urlpatterns = [
	path('', views.index, name="index"),
	# path('chatroom/', views.chatRoom, name="chatRoom"),
	path("<str:room_name>/", views.chatRoom, name="chatRoom"),
]