""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
# Not Applicable

""" Internal Package Imports """
from Data_Base.models import (Artist, Album, Song)

"""

 Data_Base/Data/Prime.py

 Author:      Matthew J Swann;              
 Version:     1.0
 Last Update: 2013-04-17
 Update By:   Matthew J Swann
 
 Primary data import scheme.

 """

def main():
    
    """
     {
        Artist One
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Jason',
                        last_name  = 'Aldean'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Night Train',
                        genre = 'C',
                        year = 2012,
                        price = 19.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = '1994'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Night Train'
            )
        
    Song.objects.create(
        album = current_album,
        name  = 'The Only Way I Know'
            )
    
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'My Kinda Party',
                        genre = 'C',
                        year = 2010,
                        price = 14.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'My Kinda Party'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Dirt Road Anthem'
            )
    
    """
     {
        Artist Two
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Disturbed',
                        last_name  = ''                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Indestructible',
                        genre = 'K',
                        year = 2008,
                        price = 16.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Indestructible'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Inside the Fire'
            )
        
    Song.objects.create(
        album = current_album,
        name  = 'Divide'
            )
    
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Ten Thousand Fists',
                        genre = 'K',
                        year = 2005,
                        price = 11.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Ten Thousand Fists'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Sons of Plunder'
            )
    
    """
     {
        Artist Three
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Seether',
                        last_name  = ''                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Holding Onto Strings Better Left to Fray',
                        genre = 'A',
                        year = 2011,
                        price = 19.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Country Song'
            )

    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'One Cold Night',
                        genre = 'A',
                        year = 2006,
                        price = 11.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Gasoline (Live)'
            )
    
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Finding Beauty in Negative Spaces',
                        genre = 'A',
                        year = 2007,
                        price = 13.49
                            )
        
    Song.objects.create(
        album = current_album,
        name  = 'Fake It'
            )
    
    """
     {
        Artist Four
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Norah',
                        last_name  = 'Jones'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Come Away With Me',
                        genre = 'P',
                        year = 2002,
                        price = 9.79
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Dont Know Why'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Cold Cold Heart'
            )
    
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'New York City',
                        genre = 'P',
                        year = 2003,
                        price = 21.99
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'New York City'
            )
    
    """
     {
        Artist Five
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Marshall',
                        last_name  = 'Mathers'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'The Re-Up',
                        genre = 'R',
                        year = 2006,
                        price = 12.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'You Dont Know'
            )

    Song.objects.create(
        album = current_album,
        name  = 'Jimmy Crack Corn'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'No Apologies'
            )
    
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Relapse',
                        genre = 'R',
                        year = 2009,
                        price = 13.89
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Beautiful'
            )
    
    """
     {
        Artist Six
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'TOOL',
                        last_name  = ''                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Ten Thousand Days',
                        genre = 'U',
                        year = 2008,
                        price = 15.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Wings for Marie (Part One)'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Wings for Marie (Part Two)'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'The Pot'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Jambi'
            )
    
    """
     {
        Artist Seven
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Infected',
                        last_name  = 'Mushroom'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Classical Mushroom',
                        genre = 'T',
                        year = 2000,
                        price = 12.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Disco Mushroom'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Dracul'
            )
    
    """
     {
        Artist Seven
     }
     """
    current_artist = Artist.objects.create(
                        first_name = '2',
                        last_name  = 'Cellos'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = '2 CELLOS',
                        genre = 'X',
                        year = 2011,
                        price = 18.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Welcome to the Jungle'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Dracul'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Smells Like Teen Spirit'
            )
    
    """
     {
        Artist Eight
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Clint',
                        last_name  = 'Mansell'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'DOOM',
                        genre = 'S',
                        year = 2005,
                        price = 13.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'First Person Shooter'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'You Know What You Are'
            )
    
    """
     {
        Artist Nine
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'Lindsey',
                        last_name  = 'Stirling'                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'Lindsey Stirling',
                        genre = 'X',
                        year = 2012,
                        price = 18.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Crystallize'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Shadows'
            )
    
    """
     {
        Artist Ten
     }
     """
    current_artist = Artist.objects.create(
                        first_name = 'A Perfect Circle',
                        last_name  = ''                   
                            )
     
    current_album  = Album.objects.create(
                        artist = current_artist,
                        name = 'emotive',
                        genre = 'A',
                        year = 2005,
                        price = 13.39
                            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Passive'
            )
    
    Song.objects.create(
        album = current_album,
        name  = 'Lets Have a War'
            )
    
if __name__ == '__main__':
    pass