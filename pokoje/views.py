from django.shortcuts import render
from .models import Pokoje
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.

@login_required(login_url="/login")
def home(request):
	return render(request, 'pokoje/home.html', {})
	
def admin(request):
	return render(request, 'pokoje/admin.html', {})

def pokoje_views(request):
	mypokoje_views = Pokoje.objects.all().values()
	template = loader.get_template('Homepage.html')
	context = {
		'mypokoje_views': mypokoje_views,
		
	}
	return HttpResponse(template.render(context, request))

def dashboard(request):
	return render(request, 'pokoje/dashboard.html', {})
