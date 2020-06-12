from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=200)
    venue=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    event_date=models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
