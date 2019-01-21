from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
	return HttpResponse("Ranco says hey there partner!")
