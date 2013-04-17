""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
from django.contrib import admin

"""     Internal Package Imports    """
from Data_Base.models import (Artist,
                              Album,
                              Song)

"""

 Control/admin.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Code for the Django admin site.

 """


class ArtistAdmin(admin.ModelAdmin):
    list_display  = ('id', 'last_name', 'first_name')
    search_fields = ['last_name', 'first_name']
    ordering      = ['last_name']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('first_name', 'last_name')
                 }),)
    
class AlbumAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'artist', 'year', 'genre')
    list_filter   = ('genre',)
    search_fields = ['name', 'artist']
    ordering      = ['name', 'artist']
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('name', 'artist', 'genre', 'year', 'price',
                        'available')
                 }),)   
    
class SongAdmin(admin.ModelAdmin):
    list_display  = ('name', 'album')
    search_fields = ['name',]
    ordering      = ['name',]
    fieldsets     = (               
        ( 'Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields' : ('name', 'album')
                 }),)  

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)