# This is a silly shitty game to try out everything I learned (and more)
# The exercise forced me to try this import module thing (reference to ex 13)

from sys import argv

if len(argv) != 3:
    print "You didn't insert three arguments"
    exit()
    
script, name_user, surname_user = argv

print "\nWELCOME"
print "Today the player is: %s %s\n" % (name_user.upper(), surname_user.upper())

# I declare three global variables

MAX_ATTEMPTS = 4 # this allows the user to retype 3 times. You can reset here the max nuber of attempts.
ARROW = "\n--> "
READING_LINE = "************************************************"

POSITIONS = ['black_room', 'red_room', 'white_room', 'start', 'black_room_guitar']
start_options = [['black', 'b', '1', 'right'],['white','w','2', 'middle'],['red','r', '3', 'left']]
red_options = [['scared', 'sad', 'Scared', 'meh'],['yo', 'ok', 'Happy', 'happy']]
black_options = [['1', 'guitar', 'give', 'to give me their guitar'], ['2', 'to stop playing', 'to stop', 'stop'],['3','the exist', 'the way out', "where's the exist"]]
guitar_options = [['play', 'play the guitar', 'make some music', 'solo', 'play a solo'], ['destroy', 'break', 'crash', 'break it', 'destroy it', 'crash it']]    
    
# I declare all the functions

def print_end():    # it prints end title once the 'game' finishes
    print "\n\t\t\t******* END OF THE GAME *******\n"

def flatten(options):
    """It takes a list of lists and flatten into a flat list"""
    flat_list = [item for sublist in options for item in sublist]
    return flat_list
    
def entry_is_acceptable(entry, options):    # this checks if any user_entry is acceptable by checking a list of lists
    """check if the user_entry is within the acceptable options and returns true or false"""
    acceptable_entry = False 
    for element in flatten(options):
        if element == entry:
            acceptable_entry = True   
            break   # optimization         
    return acceptable_entry 

def three_entry_attempts(options, position):    # it allows three attempts to type again 
    """This function is called in case the user entried a wrong option, it give 3 attemps before loosing"""
    print "What you typed doesn't make sense!"
    
    for number_attempt in range(1, MAX_ATTEMPTS):  # MAX_ATTEMPTS is set at the beginning
        
        if MAX_ATTEMPTS - number_attempt == 1:
            user_entry = raw_input("You have %d attempt to re-type... otherwise you loose! %s" % (MAX_ATTEMPTS - number_attempt, ARROW))
        
        else:
            user_entry = raw_input("You have %d attempts to re-type... otherwise you loose! %s" % (MAX_ATTEMPTS - number_attempt, ARROW))
        print READING_LINE
        
        if entry_is_acceptable(user_entry, options) and position == "start":
            print "Finally you typed right (you are in start)"
            next_move(user_entry, options, "start")
            return user_entry
            
        elif entry_is_acceptable(user_entry, options) and position == "black_room":
            print "Finally you typed right (you are in black)"
            next_move(user_entry, options, "black_room")
            return user_entry
            
        elif number_attempt == MAX_ATTEMPTS-1:
            print "You're ***dead***. Learn how to read and type... !"
            print_end()
            
        else:
            print "I DON'T GET YOU! Try again\n!"      

def guitar_scene():
    print "They give you one of their guitars."
    guitar_entry = raw_input("Do you play it or destroy it?" + ARROW).lower()
    print READING_LINE
    
    if entry_is_acceptable(guitar_entry, guitar_options):
        next_move(guitar_entry, guitar_options, "black_room_guitar")
    else:
        print "What did you type?"
        print "Never piss off metalheads and waste their time with your nonsense typing"
        print_end()
        
def black_room(): 
    print "You are in the darkest place of all, and you are sorrounded by metalheads with skull-shaped guitars."
       
    black_user_entry = raw_input("""What do you ask them?:
    
    1. To give you one of their guitars
    2. To stop playing
    3. Where's the exit 
    """ + ARROW).lower()
    print READING_LINE

    if entry_is_acceptable(black_user_entry, black_options): 
        next_move(black_user_entry, black_options, "black_room")
        
    else:
        three_entry_attempts(black_options, "black_room")

def white_room():   # inside the white_room
    print "You're in Paradise... enjoy your sweet death!"
    print_end()

def join_communism():   # when you join communism in red_room
    print "You win!"
    print "You join an amazing communist community!"
    print "Viva la rivoluzione!"
    print_end()
        
def payment():
    print "You are scared or confused and this has pissed off all communists."
    print "They caught and a communist asks you:"
    user_entry = raw_input("\'How much are you willing to pay us for letting you free?\'" + ARROW)
    print READING_LINE
    
    while not user_entry.isdigit():
        user_entry = raw_input("You didn't type a  number. Please, type the number of money you're willing to pay:" + ARROW)
    
    if user_entry.isdigit() == True and int(user_entry) >= 50:
        print "So you like using your generous capital to buy your way through life...?"
        print "We don't like that..."
        print "The communists wrapped you in a bag and sent you somewhere..."        
        white_room()
        
    elif user_entry.isdigit() == True and 0 < int(user_entry) < 50:
        print "Wow! Less then 50 bucks for saving your ass??"
        print "So...you don't buy your way through life! And you are probably poor!"
        print "We like you! <3 <3 <3"
        join_communism()
             
def red_room(): 

    red_user_entry = raw_input("Now you're in a passionate communist community... are you scared or happy?" + ARROW)
    print READING_LINE
    
    if entry_is_acceptable(red_user_entry, red_options) == True: 
        next_move(red_user_entry, red_options, "red_room")  
        
    else:
        print "Communists don't understand you, they think you're a spy."
        print "The communists wrapped you in a bag and sent you somewhere..." 
        black_room() 

def next_move(entry, acceptable_options, current_position):
    """it goes to the next move based on comparison between user_entry and the options"""
    
    if current_position == "start": # next move block from start
        for sublist in acceptable_options:
            for index in range(0, len(sublist)):
            
                if sublist[index] == entry and sublist == acceptable_options[0]:
                    black_room()
                    break
                
                elif sublist[index] == entry and sublist == acceptable_options[1]:
                    white_room()
                    break
            
                elif sublist[index] == entry and sublist == acceptable_options[2]:
                    red_room()
                    break
                    
    elif current_position == "red_room":    # next move from red_room
       
        for sublist in acceptable_options:
            for index in range(0, len(sublist)):
                
                if sublist[index] == entry and sublist == acceptable_options[0]:
                    payment()
                    break
                        
                elif sublist[index] == entry and sublist == acceptable_options[1]:
                    join_communism()
                    break  
        
    elif current_position == "black_room":  # next move from black_room
        
        for sublist in acceptable_options:
            for index in range(0, len(sublist)):
                
                if sublist[index] == entry and sublist == acceptable_options[0]:
                    guitar_scene()
                    break
                
                elif sublist[index] == entry and sublist == acceptable_options[1]:
                    print "How you dare!"
                    print "Now they play so much and loud that you die for decibels overdose."
                    print_end()
                    break
            
                elif sublist[index] == entry and sublist == acceptable_options[2]:
                    print "Surprisingly, they stop playing and gently guide you to some stairs..."
                    print "some music play in the background..."
                    print "... it\'s \'stairway to heaven\'..."
                    white_room()
                    break  
                    
    elif current_position == "black_room_guitar": # next move from taking guitar
    
        for sublist in acceptable_options:
            for index in range(0, len(sublist)):  
                if sublist[index] == entry and sublist == acceptable_options[0]:
                    print "Good one - make sure you play a metal song!"
                    print "Metalheads will welcome you by headbanging."
                    print_end()
                    
                elif sublist[index] == entry and sublist == acceptable_options[1]:
                    print "You are not a really smart guy..."
                    print "They crash you all at once in a mosh pit..."
                    white_room()  
                                        
def start_game():   # starting function that shows starting text and calls first next_move to enter the doors
    print "\t\t\t******* START OF THE GAME *******\n"
    print """You just woke up in a strange place, and you are alone. There's nothing but three colorful doors in front of you:\n
    \t 1. a black door framed with skulls on the right
    \t 2. a white angelic door in the middle
    \t 3. and, on the left, a red door with many fists.\n"""
    
    
    start_user_entry = raw_input("Choose a door to escape from this dooming loneliness." + ARROW).lower() # ask user to decide
    print READING_LINE
    
    if entry_is_acceptable(start_user_entry, start_options) == True:
        next_move(start_user_entry, start_options, "start")
               
    else:
        three_entry_attempts(start_options, "start")

start_game() # I run the game from here

