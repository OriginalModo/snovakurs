from django.db import models
from django.urls import reverse_lazy, reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('one_book', kwargs={'id_book': self.id})