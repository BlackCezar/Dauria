from django.contrib import admin
from main.models import news
from main.models import comments

admin.site.register(news)
admin.site.register(comments)
