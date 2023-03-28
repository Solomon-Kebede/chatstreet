from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('index/', views.index, name="index"),
	path('chatroom/', views.chatRoom, name="chatroom"),
	path('logout/', auth_views.LogoutView.as_view(next_page='loginaccount'), name="logout")
	# path("<str:room_name>/", views.chatRoom, name="chatroom"),

]
