from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from .forms import *
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.


# def storege_file(file):
#     with open('gallery_tpm/new_image.jpg', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)

class GalleryView(View):
    def get(self, request):
        form = GalleryUploadFile()
        return render(request, 'gallery/load_file.html', {'form': form})

    def post(self, request):
        form = GalleryUploadFile(request.POST, request.FILES)
        if form.is_valid():
            # storege_file(request.FILES['image'])
            # storege_file(form.cleaned_data['image'])
            new_image = Gallery(image=form.cleaned_data['image'])
            new_image.save()
            return HttpResponseRedirect('load_image')
        return render(request, 'gallery/load_file.html', {'form': form})

class CreateGalleryView(CreateView):
    model = Gallery
    # fields = '__all__'
    form_class = GalleryUploadFile
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'


class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    # context_object_name = 'records'