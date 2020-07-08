from django import forms

from .models import Photo


class UploadPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'desc','category_name','image']
        # exclude = ['upload_by']


        # 'upload_by'
