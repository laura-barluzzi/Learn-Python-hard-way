class Song(object):
    def __init__(self, lyrics, author):     
        self.lyrics = lyrics        
        self.author = author
   
    def sing_me_a_song(self):       
        if type(self.lyrics) is str:
            print self.lyrics
            print "\t\t\t\t - written by %s\n" % (self.author)
            
        elif type(self.lyrics) is list:
            for line in self.lyrics:
                print line
            print "\t\t\t\t - written by %s\n" % (self.author)
        else:
            print "You didn't enter a text"
            
happy_bday = Song(["Happy Birthday to you",     
                   "I don't want to get sued", 
                   "So I'll stop right there"], "Zio Billy")
                   
bulls_on_parade = Song(["They rally around the family",    
                        "With pockets full of shells"], "Pimpy Shaggy")
                        
sure_looks_good_to_me = ["Life is cheap, bittersweet",    
                              "... but it tastes good to me"]                  

testo = "Parlami, come il vento fra gli alberi... \ndimmi se fare qualcosa, se mi stai sentendo"
     
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song() 

Song(sure_looks_good_to_me, "Alicia Keys").sing_me_a_song()   

Song(testo, "Elisa").sing_me_a_song()
