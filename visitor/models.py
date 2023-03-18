from django.db import models

class Visitor(models.Model):
    ip_address = models.CharField(max_length=20)
    visit_time = models.DateTimeField(auto_now_add=True)
