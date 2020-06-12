
from django.db import models
from datetime import datetime
from seller.models import Seller
from events.models import Event
from category.models import Category
from randomid.models import randomId

# Create your models here.

        
class Ticket(models.Model):
    code=models.OneToOneField(randomId, on_delete=models.DO_NOTHING)
    seller=models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    Event=models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    Category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price=models.IntegerField()   
    # photo=models.ImageField(upload_to='photos/%Y/%M/%D/')
    list_date=models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Event



