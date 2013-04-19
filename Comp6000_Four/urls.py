""" Python Package Support """
# Not Applicable

""" Django Package Support """
from django.conf.urls import patterns, include, url
from django.contrib import admin

""" Internal Package Imports """
# Imported below.

"""

 Comp6000_Four/urls.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-19
 Update By:   Matthew J Swann
 
 Code for website urls.

 """

admin.autodiscover()

urlpatterns = patterns('',

    # ADMIN PAGES
    url(r'^$', 'Data_Base.views.homepage', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # COMMIT PAGES
    url(r'^add/album/$', 'Data_Base.views.commit_album', name='commit_album'),
    url(r'^add/artist/$', 'Data_Base.views.commit_artist', name='commit_artist'),
    url(r'^add/song/$', 'Data_Base.views.commit_song', name='commit_song'),
    
    # SEARCH PAGES
    url(r'^search/album/$', 'Data_Base.views.ajax_album_home', name='ajax_album_home'),
    url(r'^search/artist/$', 'Data_Base.views.ajax_artist_home', name='ajax_artist_home'),
    url(r'^search/song/$', 'Data_Base.views.ajax_song_home', name='ajax_song_home'),    
    url(r'^search/album/(\w+)/$', 'Data_Base.views.ajax_album_search', name='ajax_album_search'),
    url(r'^search/artist/(\w+)/$', 'Data_Base.views.ajax_artist_search', name='ajax_artist_search'),
    url(r'^search/song/(\w+)/$', 'Data_Base.views.ajax_song_search', name='ajax_song_search'),      

    # DISPLAY PAGES
    url(r'^album/(\d+)/$', 'Data_Base.views.specific_album', name='specifc_album'),
    url(r'^artist/(\d+)/$', 'Data_Base.views.specific_artist', name='specific_artist'),
    url(r'^song/(\d+)/$', 'Data_Base.views.specific_song', name='specific_song'),
)
