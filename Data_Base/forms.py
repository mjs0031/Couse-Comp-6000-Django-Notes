""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django import forms

""" Internal Package Imports """
from Control.choice_lists import GENRE_TYPES
from Data_Base.models import (Album, Artist, Song)

"""

 Data_Base/forms.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-18
 Update By:   Matthew J Swann
 
 Code for the website forms and inherent functionality.

 """
 
 
"""
 ALBUM Form
"""
class AlbumForm(forms.Form):
    artist    = forms.ModelChoiceField(queryset=Artist.objects.all())
    name      = forms.CharField(max_length=30)
    genre     = forms.ChoiceField(choices=GENRE_TYPES, widget=forms.Select)
    year      = forms.IntegerField()
    price     = forms.DecimalField(max_digits=10, decimal_places=2)
    available = forms.BooleanField(required=False)


"""
 ARTIST Form
"""            
class ArtistForm(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15, required=False)
 
        
"""
 SONG Form
"""     
class SongForm(forms.Form):
    album = forms.ModelChoiceField(queryset=Album.objects.all())
    name = forms.CharField(max_length=30)