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
    class Meta:
        model = Album
        fields = (
            'name',
            'genre',
            'year',
            'price',
            'available',
        )
        widgets = {
            'name': forms.widgets.TextInput(attrs={'placeholder': 'Name'}),
            'genre': forms.Select(choices=GENRE_TYPES, attrs={'class': 'selectpicker'}), 
            'year': forms.widgets.TextInput(attrs={'placeholder': 'Year'}),
            'price': forms.widgets.TextInput(attrs={'placeholder': 'Price'}),
            'available': forms.widgets.CheckboxInput(attrs={'placeholder': 'Available'}),
        }

"""
 ARTIST Form
"""        
class ArtistForm(forms.Form):
    class Meta:
        model = Artist
        fields = (
            'first_name',
            'last_name',
        )
        widgets = {
            'first_name': forms.widgets.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        
"""
 SONG Form
"""        
class SongForm(forms.Form):
    class Meta:
        model = Song
        fields = (
            'name',
        )
        widgets = {
            'name': forms.widgets.TextInput(attrs={'placeholder': 'Name'}),
        }