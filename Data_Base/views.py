""" Python Package Imports """
import random, string, unicodedata

""" Django Package Imports"""
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

""" Internal Package Imports """
from Control.choice_lists import GENRE_TYPES
from Data_Base.models import (Album, Artist, Song)
from Data_Base.forms import (AlbumForm, ArtistForm, SongForm)


"""

 Data_Base/views.py

 Author:      Matthew J Swann;               
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Code for the website forms and inherent functionality.

 """

"""
 {
  ADMIN BLOCK
 }
 """
def homepage(request):
    return render_to_response('homepage.html')


"""
 {
  COMMIT BLOCK
 }
 """
def commit_album(request):  
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            Album.objects.create(
                artist    = Artist.objects.get(pk=1),
                name      = form.cleaned_data['name'],
                genre     = form.cleaned_data['genre'],
                year      = form.cleaned_data['year'],
                price     = form.cleaned_data['price'],
                available = form.cleaned_data['available'],
                        )
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm()
    return render_to_response('add_album.html', locals())


def commit_artist(request):  
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            Artist.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name  = form.cleaned_data['last_name'],
                        )
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
    return render_to_response('add_artist.html', locals())


def commit_song(request):  
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            Song.objects.create(
                album = Album.objects.get(pk=1),
                name  = form.cleaned_data['name'],
                        )
            return HttpResponseRedirect('/')
    else:
        form = SongForm()
    return render_to_response('add_song.html', locals())


"""
 {
  SEARCH BLOCK
 }
 """
def ajax_album_home(request):
    return render_to_response('search_album.html')

def ajax_album_search(request, searchString):
    found = True 
    results = Album.objects.filter(name__startswith=searchString)
    if not results:
        results = Album.objects.all()
        found = False
    return render_to_response('render_album.html', {
                                "results": results,
                                "found": found,
                                })


def ajax_artist_home(request):
    return render_to_response('search_artist.html')

def ajax_artist_search(request, searchString):
    found = True 
    results = Artist.objects.filter(last_name__startswith=searchString)
    if not results:
        results = Artist.objects.all()
        found = False
    return render_to_response('render_artist.html', {
                                "results": results,
                                "found": found,
                                })


def ajax_song_home(request):
    return render_to_response('search_song.html')

def ajax_song_search(request, searchString):
    found = True 
    results = Song.objects.filter(name__startswith=searchString)
    if not results:
        results = Song.objects.all()
        found = False
    return render_to_response('render_song.html', {
                                "results": results,
                                "found": found,
                                })
    
    
