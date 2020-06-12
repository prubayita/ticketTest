from django.db import models
import random
import string
import qrcode
# Create your models here.

class randomId(models.Model):
    
    #making of random string and use them to generate qr code
    finalCode = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(8))
    qr= qrcode.make(finalCode)
    
    #code=models.CharField(finalCode, primary_key=True, null=False, unique=True)
    code=models.ImageField(qr.save(finalCode+'.png'), upload_to='qrcodeMedia',)
    def __str__(self):
        return self.code

        