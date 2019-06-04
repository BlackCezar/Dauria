from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from main.models import news
from main.models import comments

urlpatterns = [
    url('about', views.about, name="about"),
    url('team', views.team, name="team"),
    url('contact', views.contact, name="contact"),
    url('comment', ListView.as_view(queryset=comments.objects.all().order_by("-data_comments")[:5],template_name="main/comment.html")),
    url('news', ListView.as_view(queryset=news.objects.all().order_by("-data")[:20],template_name="main/news.html")),
    url('', views.index, name="index"),
]
