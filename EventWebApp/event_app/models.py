from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    #Fields
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

        
        #Methods
    def __str__(self):
        return self.title