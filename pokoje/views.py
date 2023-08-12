from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request, 'pokoje/home.html', {})
	
def admin(request):
	return render(request, 'pokoje/admin.html', {})
