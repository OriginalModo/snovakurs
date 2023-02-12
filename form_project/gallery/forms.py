from django import forms
from .models import *

class GalleryUploadFile(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
    # image = forms.FileField()

