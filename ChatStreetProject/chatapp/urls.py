from django.urls import path
from . import views
# for image files
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('index/', views.index, name="index"),
	path('chatroom/', views.chatRoom, name="chatroom"),
	# path("<str:room_name>/", views.chatRoom, name="chatroom"),

]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)