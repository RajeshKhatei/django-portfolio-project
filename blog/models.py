from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100] + '...'

    def publish_date_format(self):
        return self.publish_date.strftime('%b %e %Y')
