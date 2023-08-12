from django.shortcuts import render
from .models import Pokoje
from django.http import HttpResponse
from django.template import loader

# Create your views here.

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
