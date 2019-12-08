from django.db import models


class Job(models.Model): # allows this object to database
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
