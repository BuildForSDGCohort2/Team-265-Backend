from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from posts.models import Post

def home_page(request):
    user = request.user
    qs = Post.objects.all()[:5]
    if request.user.is_authenticated:
        greeting = "Hey, {}. Checkout the requirements:".format(user)
        context = {"my_greeting": greeting, "my_list": ["Python3", "Django 2.2", "MySQL", "Heroku"], "post": qs} #
    else:
        greeting = "Hey, {}. Please sign up for awesome content!".format(user)
        context = {"my_greeting": greeting, "my_list": ["Python3", "Django 2.2", "MySQL", "Heroku"]}
    return render(request, "home.html", context)

def about_page(request):
    user3 = request.user
    return render(request, "register.html", {"user": user3})
    #return HttpResponse("<h1>ABOUT THE APP</h1>")

def contact_page(request):
    #user = request.user
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    else:
        print("NOne")
    context = {"title": "Contact Us", "form": form}
    return render(request, "form.html", context)
    #return HttpResponse("<h1>PLEASE CONTACT US</h1>")    