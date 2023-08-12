from django.db import models
from django.contrib.auth.models import User

# Create your models here.\



class Pokoje(models.Model):
	nazwapokoju = models.CharField(max_length=200)
	wartosc1 = models.IntegerField()
	wartosc2 = models.IntegerField()
	wartosc3 = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nazwapokoju
