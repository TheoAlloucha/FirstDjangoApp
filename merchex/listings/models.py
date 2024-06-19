from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    # La Methode Magique "__str__"
    # sert a renvoyé la chaine de caractère dans le panel admin
    # et non "Band object (id number)"

    # Nous avons modifié la façon dont un Band est représenté sous forme de chaîne de caractères
    # en utilisant la méthode __str__
    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(default=0,
                                             validators=[MinValueValidator(1900), MaxValueValidator(2021)]
                                             )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    def __str__(self):
        return f'{self.title}'
    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(default=0,
                                      validators=[MinValueValidator(1900), MaxValueValidator(2021)]
                                      )
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
