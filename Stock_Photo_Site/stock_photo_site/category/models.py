from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key = True, null=False, default = None)

    def __str__(self):
        return self.category_name

    # models.TextField()