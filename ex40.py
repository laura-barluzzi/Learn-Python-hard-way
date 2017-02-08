
class Song(object):
    def __init__(self, lyrics):     # it create the empty object of self for creating variables and lyrics imported 
        self.lyrics = lyrics        # I create a variable (like always using self.) with the value of the lyrics imported
        
    def sing_me_a_song(self):       # I create a function that prints all the line in the self.lyrics variable, nontheless the lyrics imported
        for line in self.lyrics:
            print line
            
            
happy_bday = Song(["Happy Birthday to you",     # instantiate the class importing a list of strings as 'lyrics' assigning to 'happy_bday'var
                   "I don't want to get sued", 
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",     # that same, but this time we import a different list as 'lyrics'
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 

# study drill
                       
sure_looks_good_to_me = ["Life is cheap, bittersweet",     # the same, again it changes only the imported 'lyrics' value
                              "... but it tastes good to me"]                  
                        
Song(sure_looks_good_to_me).sing_me_a_song() 



  
