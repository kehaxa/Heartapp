from django.db import models

# Create your models here.
class UsersDB(models.Model):
	login_models = models.CharField(max_length=200)
	password_models = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
