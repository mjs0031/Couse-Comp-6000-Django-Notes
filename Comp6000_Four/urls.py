""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Internal Package Imports """
#from Data_Base.models import 

"""

 Comp6000_Four/urls.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Code for website urls.

 """

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
