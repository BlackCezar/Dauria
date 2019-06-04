from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def news(request):
    return render(request, "main/news.html")

def team(request):
    return render(request, "main/team.html")

def contact(request):
    return render(request, "main/contact.html")

def comment(request):
    return render(request, "main/comment.html")

# Create your views here.
