from django.db import models

class comments(models.Model):
    person = models.CharField(max_length = 120)
    city = models.TextField()
    text = models.TextField()
    data_comments = models.DateTimeField()

    def __str__(self):
        return self.person

class news(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.title

    
