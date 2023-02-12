from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify



# Create your models here.

class Actor(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField('DressingRoom', on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)


    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse_lazy('one_actor', kwargs={'pk':self.pk})

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField(default='sugardaddy')
    # slug = models.SlugField(default='', null=False, db_index=True, unique=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} '

    def get_absolute_url(self):
        return reverse_lazy('one_director', kwargs={'pk':self.pk})

class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()


    def __str__(self):
        return f'{self.floor} {self.number}'


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True, unique=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    # director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='movie')
    actors = models.ManyToManyField(Actor)
    # currency = models.CharField(max_length=5)


    def __str__(self):
        return f'{self.name} {self.rating} {self.year}'


    def get_absolute_url(self):
        return reverse_lazy('one_movie', kwargs={'slug_movie': self.slug})
        # return reverse('one_movie', args=[self.id])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie,self).save(*args, **kwargs)

