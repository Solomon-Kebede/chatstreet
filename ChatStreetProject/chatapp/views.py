from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def chatRoom(request, room_name):
    return render(request, 'room.html', {"room_name": room_name})

def login(request):
    return render(request, 'registration/login.html')