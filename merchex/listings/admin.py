from django.contrib import admin
from listings.models import Band, Listing


# Register your models here.
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # liste les champs que nous voulons sur l'affichage de la liste


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'sold', 'band_id')  # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)  # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Listing, ListingAdmin)
