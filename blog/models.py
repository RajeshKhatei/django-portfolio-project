from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
