""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django import forms
from django.contrib.localflavor.us.us_states import STATE_CHOICES


""" Internal Package Imports """
#from Data_Base.models import 

"""

 Data_Base/forms.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Code for the website forms and inherent functionality.

 """
 
"""
Form used to choose knoll type and setup contact information for the knoll (same for all three types). This
involves instantiate the entity object as well as the PersonnelData object to represent the ownership between
the knoll and its creator (level 3 permission).
"""
class KnollContactForm(forms.Form):
    knoll_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selectpicker'}))
    name = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Name'}))
    addressLineOne = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Address Line 1'}))
    addressLineTwo = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Address Line 2'}))
    city = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'City'}))
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'selectpicker'}))
    zipCode = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Zip'}))
    phone = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone'}))
    avatar = forms.ImageField(widget=forms.widgets.FileInput())