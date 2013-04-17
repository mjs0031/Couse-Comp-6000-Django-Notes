""" Python Package Imports """
from datetime import datetime

""" Django Package Imports """
from django.db import models

""" Internal Package Imports """
from Control.choice_lists import GENRE_TYPES

"""

 Data_Base/models.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Code for the database tables and inherent functionality.

 """


"""
 ARTIST Class -- Represents a musical artist
 """    
class Artist(models.Model):
    # Natural Fields
    first_name      = models.CharField(max_length=15)
    last_name       = models.CharField(max_length=15, blank=True)
       
    def __unicode__(self):
        if not (self.last_name == ''):
            return '%s, %s' % (self.last_name, self.first_name)
        else:
            return '%s'     % (self.first_name)

    
    class Meta:
        verbose_name        = "Artist"
        verbose_name_plural = "Artists"
    
    
class OrderedArtist(Artist):
    class Meta:
        verbose_name        = "Ordered Artist"
        verbose_name_plural = "Ordered Artists"
        ordering            = ['last_name', 'first_name']
        proxy               = True
       
        
"""
 ALBUM Class -- Represents a musical album
 """    
class Album(models.Model):
    # Keyed Fields
    artist    = models.ForeignKey(Artist)
    # Natural Fields
    name      = models.CharField(max_length=30)
    genre     = models.CharField(max_length=1, choices=GENRE_TYPES, default='U')
    year      = models.DecimalField(default=0, max_digits=10, decimal_places=0) 
    price     = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
       
    def __unicode__(self):
        return '%s: %s (%s)' % (self.name, self.artist, self.year)
    
    class Meta:
        verbose_name        = "Album"
        verbose_name_plural = "Albums"
    
    
class OrderedAlbum(Album):
    class Meta:
        verbose_name        = "Ordered Album"
        verbose_name_plural = "Ordered Albums"
        ordering            = ['name', 'year']
        proxy               = True
        
"""
 SONG Class -- Represents a song
 """    
class Song(models.Model):
    # Keyed Fields
    album = models.ForeignKey(Album)
    # Natural Fields
    name  = models.CharField(max_length=30)
       
    def __unicode__(self):
        return '%s: %s' % (self.album, self.name)
    
    class Meta:
        verbose_name        = "Song"
        verbose_name_plural = "Songs"
    
    
class OrderedSong(Song):
    class Meta:
        verbose_name        = "Ordered Song"
        verbose_name_plural = "Ordered Songs"
        ordering            = ['album', 'name']
        proxy               = True