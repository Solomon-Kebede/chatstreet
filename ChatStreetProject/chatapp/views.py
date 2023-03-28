from django.shortcuts import render
from .models import ContactInfo
from django.contrib.auth.models import User


# Create your views here.
def index(request):
	return render(request, 'chat/index.html')

def chatRoom(request):
    contact_info = ContactInfo.objects.all()
    users = User.objects.all()
    return render(request, 'chat/room.html', {'users': users, "contact_info": contact_info})

#def contact_list(request):
#    return render(request, 'chat/room.html', {'name': 'Contact')
