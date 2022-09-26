from django.db import models

# Create your models here.

class TooDoo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(blank=False)
    status = models.CharField(max_length=100, blank=False)
    place = models.CharField(max_length=100, null=True,blank=True)


    def __str__(self):
        return self.title