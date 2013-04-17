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

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)