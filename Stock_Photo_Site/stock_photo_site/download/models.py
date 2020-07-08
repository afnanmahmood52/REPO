from django.contrib.auth.models import User
from django.db import models
from photo.models import Photo
import datetime


# Create your models here.
class Download(models.Model):

    download_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    filename = models.ForeignKey(Photo, default=None, on_delete=models.CASCADE)
    date_stamp = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.filename