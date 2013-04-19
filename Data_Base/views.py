""" Python Package Imports """
import random, string, unicodedata

""" Django Package Imports"""
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render

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
            pointer = Album.objects.create(
                artist    = form.cleaned_data['artist'],
                name      = form.cleaned_data['name'],
                genre     = form.cleaned_data['genre'],
                year      = form.cleaned_data['year'],
                price     = form.cleaned_data['price'],
                available = form.cleaned_data['available'],
                        )
            return HttpResponseRedirect('/album/%s' % (pointer.id))
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', RequestContext(request, {
                                                        'form': form,                
                                                        }))

def commit_artist(request):  
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            pointer = Artist.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name  = form.cleaned_data['last_name'],
                        )
            return HttpResponseRedirect('/artist/%s' % (pointer.id))
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', RequestContext(request, {
                                                        'form': form,               
                                                        }))

def commit_song(request):  
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            pointer = Song.objects.create(
                album = form.cleaned_data['album'],
                name  = form.cleaned_data['name'],
                        )
            return HttpResponseRedirect('/song/%s' % (pointer.id))
    else:
        form = SongForm()
    return render(request, 'add_song.html', RequestContext(request, {
                                                    'form': form,                 
                                                    }))


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

    
"""
 {
  DISPLAY BLOCK
 }
 """    
def specific_artist(request, offset):
    offset = int(offset)
    artist = Artist.objects.get(pk=offset)
    albums = Album.objects.filter(artist=artist)
    return render_to_response('specific_artist.html', locals())

def specific_album(request, offset):
    offset = int(offset)
    album  = Album.objects.get(pk=offset)
    songs  = Song.objects.filter(album=album)
    return render_to_response('specific_album.html', locals())

def specific_song(request, offset):
    offset = int(offset)
    song   = Song.objects.get(pk=offset)
    return render_to_response('specific_song.html', locals())