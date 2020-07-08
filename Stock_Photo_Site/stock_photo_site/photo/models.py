from django.contrib.auth.models import User
from django.db import models
from django.core.files.images import get_image_dimensions
# from category.models import Category


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50,primary_key=True)
    desc = models.TextField(max_length=2000)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/',width_field='width',height_field='height')
    
    upload_by = models.ForeignKey(User, to_field='username', default=None, on_delete=models.CASCADE)

    category_name = models.ForeignKey('category.Category' , default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





