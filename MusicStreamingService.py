import abc
from datetime import datetime, date
from typing  import List


def validate_string(value, field_name):
    """Validates string values"""
    if value is None:
        raise ValueError(f"{field_name} cannot be None")
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    if not value.replace(" ", ""):
        raise ValueError(f"{field_name} cannot be an empty or blank string")

def validate_value_ascii(value,field_name):
    if not value:
        raise ValueError("Empty song title")
    #defining max length for safety
    min_len=0
    max_len=40
    if not isinstance(value,str): 
       raise TypeError("Not valid string")
    else: 
       if not value.strip():
          raise ValueError("Invalid value")
       #Song names or Artist's name can contain numbers 
       if not value.isascii():
          raise ValueError("Invalid value")
       if not min_len<len(value)<max_len:
          raise ValueError("Invalid value")     
       

class MusicOperations(abc.ABC):
    """Interface for music operation"""
    @abc.abstractmethod
    def play(self):
        pass
    
    @abc.abstractmethod
    def replay(self):
        pass
    

class MusicType(abc.ABC):
    """Interface for music genres"""
    @abc.abstractmethod
    def getMusicGenre(self):
        pass
    
class Rock(MusicType):
     def getMusicGenre(self):
         return "Rock"
        
class Classic(MusicType):
     def getMusicGenre(self):
         return "Classical"  
     
class Song(MusicOperations):
    
    def __init__(self,title:str,artist:str,length:float, genre:MusicType=None) -> None:
       self.title=title
       self.artist=artist
       self.length=length
       self.genre=genre
      
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        f_name="title"
        validate_value_ascii(value, f_name)
        self.__title=value
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        f_name="title"
        validate_value_ascii(value, f_name)
        self.__artist=value
          
    @property
    def length(self):
        return self.__length     
    

    @length.setter
    def length(self, value):
        if not value:
            raise ValueError("Invalid value")
        min_len=0.3
        max_len=10.0
        if isinstance(value, float):
           if min_len<value<max_len:
              self.__length=value
           else:
               raise ValueError("Range of length must be 0.3 - 10 minutes")
           
        else:
            raise TypeError("Invalid type")  

    def play(self):
        return f"Playing {self.title}...."
        
    def replay(self):
        return f"Replaying {self.title}.."
        
    def __str__(self)->str:
        """String represenation"""
        if self.genre:
           genre=self.genre.getMusicGenre()
           
        else:
           genre="Not mentioned"
        return f"Song: {self.title}, Artist: {self.artist}, Duration: {self.length} minutes, Genre: {genre}"


    def __repr__(self)->str:
        return f"{type(self).__name__}: {self.title}"
       
     
class Album:
    """Class album with attributes such as title, artist, and release date"""
    def __init__(self,title:str,artist:str,release_date:datetime) -> None:
         self.title=title
         self.artist=artist
         self.release_date=release_date
         self.__songs: List[Song]=[]
         
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        f_name="title"
        validate_value_ascii(value, f_name)
        self.__title=value
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        f_name="title"
        validate_value_ascii(value, f_name)
        self.__artist=value

    @property
    def songs(self):
        return self.__songs
    
    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self,value):
        if isinstance(value, date):
            self.__release_date=value
        else:
            raise TypeError("Invalid time for release date")
        

    def add_songs(self, lst_song:List[Song]):
        """Adds songs to album"""
        if not lst_song:
           raise ValueError("There is no song to add")
        if isinstance(lst_song, List):
           for song in lst_song:
               if isinstance(song, Song):
                  self.songs.append(song)
               else:
                   raise TypeError("Invalid type to add")
        else:
            raise TypeError("Invalid type ")

        
    def view_songs(self):
        """View songs in album"""
        result= f"\nSongs in album: {self.title}:\n"
        if self.songs:
           for i in self.songs:
               result+=(str(i)) + "; \n"
           return result
        else:
            return f"Empty album '{self.title}'"

    def __str__(self) -> str:
        """String representation"""
        return f"Title: {self.title}, Artist: {self.artist}, Release_date: {self.release_date}"
    
    def __repr__(self)->str:
        return f"{type(self).__name__}: {self.title}"

         

class Playlist:
    def __init__(self, name:str)->None:
        self.name=name
        self.__songs: List[Song]=[]
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str)->None:
        f_name="Playlist name"
        validate_string(value,f_name)
        self.__name=value

        
    @property
    def songs(self):
        return self.__songs
    
    def add_songs(self, lst_song:List[Song]):
        """Adds songs to playlist"""
        if not lst_song:
           raise ValueError("There is no song to add")
        if isinstance(lst_song, List):
           for song in lst_song:
               if isinstance(song, Song):
                  self.songs.append(song)
               else:
                   raise TypeError("Invalid type to add")
        else:
            raise TypeError("Invalid type ")
        
    def view_songs(self):
        """View songs in playlist"""
        result= f"Songs in playlist: {self.name}:\n"
        for i in self.songs:
            result+=(str(i)) + "; "
        return result
    
    def __str__(self)->str:
        """String represenation"""
        return f"Playlist: {self.name}"


    def __repr__(self)->str:
        return f"{type(self).__name__}: {self.name}"
    

## The program should allow users to search for and listen to songs, create and manage playlists, and view their listening history. 
class User:
        def __init__(self,name:str): 
            self.name=name
            self.__playlist: List[Playlist]=[]
            self.__listening_history: List[Song]=[]
            
        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, value):
            f_name="Name"
            validate_string(value, f_name)
            self.__name = value
        
        @property
        def playlist(self):
            return self.__playlist 
        
        @property
        def listening_history(self):
            return self.__listening_history


        def create_playlist(self, name:str, songs_toadd: List[Song]):
            """Creating playlist"""
            f_name="playist_name"
            validate_string(name, f_name)
            created_playlist=Playlist(name) #setting name for new playlist
            max_count=100 #max count to add is 100 songs
            if not songs_toadd:
               raise ValueError("There is no songs to add")
            
            if not isinstance(songs_toadd, List):
               raise ValueError("List of songs")   
            if not len(songs_toadd)<=max_count:
               raise ValueError("Max count of songs is 100")      
            else:
                for song in songs_toadd:
                    if not isinstance(song,Song):
                       raise TypeError("Invalid type to add")
                self.playlist.append(created_playlist)
                #adding songs to playlist
                created_playlist.add_songs(songs_toadd)
                
        def remove_playist(self, name:str):
            f_name="Playlist name to remove"
            validate_string(name, f_name)
            for pl in self.playlist:
                if pl.name==name:
                   self.playlist.remove(pl)
                   print(f"REMOVED playlist {name}")
                   return
                
                   
                else:
                    raise ValueError(f"{name} is absent in {self.name} playlists")
        
        def add_to_listening_history(self):
            """Adding songs to listening history"""
            if self.playlist:
                for i in self.playlist:
                    self.listening_history.append(i.songs)
            else:
                raise ValueError("There are empty playlists")
        
        def view_listening_history(self):
            """View listening history"""
            if self.listening_history:
               res_str=" "
               for i in self.listening_history:
                   res_str+=str(i)+";"
               return res_str
            else:
                return f"Empty listening history"
        
        def __str__(self):
            """String representation"""
            return f"Name: {self.name}, {self.playlist}"
            
        def __repr__(self) -> str:
            return f"{type(self).__name__}"
        
        
def main()->None:
    try:
        #constructing songs
        title="Lovesong"
        artist="Adele"
        length=float(5)
        song1=Song(title,artist, length)
        print(song1)
        
        title2="Let It Be"
        artist2="The Beatles"
        length2=float(4.45)
        song2=Song(title2,artist2, length2)
        print(song2)

        title3="title3"
        artist3=" artist3"
        length3=float(4.49)
        song3=Song(title3,artist3, length3, Classic())
        print(song3)

        title4="title4"
        artist4=" artist4"
        length4=float(3.37)
        song4=Song(title4,artist4, length4, Rock())
        
        
        #creating user
        u1=User("Mary")
        name="Favourite"
        lst_songs=[song1,song2]
        u1.create_playlist(name, lst_songs)
        print(u1)
        
        #creating user
        u2=User("Mark")
        #has 2 playlists
        name="Dancing music"
        name2="Sport music"
        lst_songs=[song3]
        lst_songs2=[song4]
        u2.create_playlist(name,lst_songs)
        u2.create_playlist(name2,lst_songs2)
        print(f"Before removing playlist {name}")
        print(u2)
        print("After removing")
        u2.remove_playist(name)
        print(u2)
        u2.add_to_listening_history()
        hist=u2.view_listening_history()
        print(f"~~~Listening history~~~\n{hist}")
        
        title5="Skyfall"
        artist5="Adele"
        length5=float(5)
        song5=Song(title5,artist5, length5)
        
        

        album_name="19"
        artist="Adele"
        dt=date(2022,12,27)
        album1=Album(album_name,artist, dt)
        print("~~~ALBUM~~~")
        print(album1)
        album1.add_songs([song1,song5])
        songs_in_album=album1.view_songs()
        print(songs_in_album)
        
        print(f"Playing....{song5.play()}")
    except Exception as e:
        print(e)

    
if __name__=="__main__":
    main()
    
    
        
    
    
        