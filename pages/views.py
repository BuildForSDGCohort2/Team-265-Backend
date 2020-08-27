from django.shortcuts import render
from django.http import HttpResponse #invoke html

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})