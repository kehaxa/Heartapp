from django.urls import path, include
from . import views
from register import views as v

urlpatterns = [
    path('', views.home, name="home"),
    path('', include('django.contrib.auth.urls')),
    path('admin/', views.admin, name="admin"),
    path("register/", v.register, name="register"),

]
