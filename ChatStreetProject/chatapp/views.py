from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def chatRoom(request):
    return render(request, 'room.html')

def login(request):
    return render(request, 'registration/login.html')