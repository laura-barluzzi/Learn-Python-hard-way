"""This is the main script for the game ex45."""


from sys import exit
from random import randint
from player import PlayerSummary
from check import CheckEntry 


ENTRY_ARROW = "\n --> "
LINE = "\n" + "*" * 30 + "\n"
        

class Start(object): 
   
    start_options = [("university", ["1", "go to university", "university"], "You went to university."), 
                     ("humble_job", ["2", "apprenticeship"], "You decided to do an apprenticeship."),
                     ("humble_job", ["3", "get a job", "go to work", "job"], "You tried to find any job.")]
           
    def take(self):        
        
        self.user_name = raw_input("What's your name? \n--> ")
        
        print "\nHi %s, welcome to LIFE DECISION TRAINER!" % (self.user_name)
        print "Life is the battlefield each of us must fight."
        print "Here you have the chance to simulate important decisions,"
        print "those decisions that most affect the course of your life."
        print LINE
        print "You are now a 17-year-old who is approaching the end of"
        print "highschool and the first major life-decision..."
        print "What do you do after high-school?"
        
        print "\n1) Go to Univerity;"
        print "2) Apprenticeship;"
        print "3) Get a job.\n"

        
        decision = raw_input("What do you do after high-school?" + ENTRY_ARROW).lower()

        check = CheckEntry(self.start_options)
        acceptable_entry, next_decision, statement = check.acceptable(decision)
               
        if acceptable_entry is False:
                    
            return check.new_attempt()  
       
        else:
        
            return next_decision, statement
            

class University(object):
    
    university_options = [("rich", ["1", "medicine"], "You studied medicine."),
                          ("rich", ["2", "computer science", "programming"], "You studied computer science"),
                          ("rich", ["3", "engineering", "engineer"], "You studied engineering."),
                          ("rich", ["4", "law"], "You studied law."),
                          ("unemployment", ["5", "others", "phylosophy", 
                                            "politics", "sociology", "art", "literature"], "You studied a non-scientifical subject.")]
                          
    def take(self):
        
        print LINE
        print "You decided to go to university, so probably you have a very strong passion."
        print "Or maybe you are simply influenced by ideas of 'success' and 'money'."
        print "Either way, you must choose a subject of the following:"

        print "\n1) Medicine;"
        print "2) Computer Science;"
        print "3) Engineering;" 
        print "4) Law;"
        print "5) Others.\n"

        
        subject = raw_input("In which subject do you graduate?"+ ENTRY_ARROW).lower()
        
        check = CheckEntry(self.university_options)  
        acceptable_entry, next_decision, statement = check.acceptable(subject)
               
        if acceptable_entry is False:
                    
            return check.new_attempt()
       
        else:
        
            return next_decision, statement
            

class HumbleJob(object):

    humble_job_options = [("love", ["1", "i like crafty jobs", "i like handy jobs"], "You did a humble job you love."),
                          ("unemployment", ["2", "i don't know"], "You were very undecided about why not to study.")]
    
    def take(self):
    
        print LINE
        print "You decided not to study and to start working."
   
        print "\n1) I like crafty and handy jobs;"
        print "2) I don't know\n"

        
        humble_job = raw_input("Did you take this decision for any of the these reasons?"+ ENTRY_ARROW).lower()
        
        check = CheckEntry(self.humble_job_options)  
        acceptable_entry, next_decision, statement = check.acceptable(humble_job)
               
        if acceptable_entry is False:
                    
            return check.new_attempt()
       
        else:
        
            return next_decision, statement
            
        
class Rich(object):

    rich_options = [("love", ["1", "donate", "help", "charities"], "You donated a lot of your capital."),
                    ("love", ["2", "invest", "buy proprieties"], "You decided to keep your money for yourself.")]
    
    def take(self):
    
        print LINE
        print "You have chosen the right career - the wealthy one! "
        print "You are now rich!"

        print "\n1) Donate money to charities;"
        print "2) Invest and/or buy proprieties.\n"

                      
        donate = raw_input("Are you going to donate or to buy proprieties?" + ENTRY_ARROW).lower()
        
        check = CheckEntry(self.rich_options)  
        acceptable_entry, next_decision, statement = check.acceptable(donate)
               
        if acceptable_entry is False:
                    
            return check.new_attempt()
       
        else:
        
            return next_decision, statement

        
class Unemployment(object):

    unemployed_options = [("love", ["yes", "y", "many", "I have hobbies"], "You were unemployed, but pursued your hobbies."),
                          ("love", ["no", "n", "meh", "not really"], "You were unemployed, and got bored and depressed.")]
    
    def take(self):
    
        print LINE
        print "Most likely you are unemployed due to your previous life decisions."
        print "Considering there are high chances you are unemployed for years,\n"
        
        hobby = raw_input("Do you have any hobby to pursue?" + ENTRY_ARROW).lower()
        
        check = CheckEntry(self.unemployed_options)
        acceptable_entry, next_decision, statement = check.acceptable(hobby)

        if acceptable_entry is False:
                    
            return check.new_attempt()
       
        else:
        
            return next_decision, statement
            
                
class Love(object):

    love_options = [("children", ["yes", "y", "oui", "sure"], "You decided to commit to someone."),
                    ("health", ["no", "n", "not sure", "never"], "You decided not to commit and to be a free rider.")]
                    
    def take(self):
        
        print LINE
        print "Everyone has to face the natural urge of passion and love. In defining your"
        print "attitude towards sexual and romantic relationshps, you may drastically"
        print "change your life.\n"
        
        commitment = raw_input("Will you committ with someone?"+ ENTRY_ARROW).lower()
                
        check = CheckEntry(self.love_options)  
        acceptable_entry, next_decision, statement = check.acceptable(commitment)
               
        if acceptable_entry is False:
                    
            return check.new_attempt()
       
        else:
        
            return next_decision, statement
            
        
class Children(object):

    children_options = [("family", ["yes", "y", "oui", "sure"], "You decided to have a family with kids."),
                        ("health", ["no", "n", "not sure", "never"], "You decided not to have kids.")]
                        
    def take(self):
        
        print LINE
        print "You decided to committ with the love of your life. You probably are wondering"
        print "if it'd be nice to build a family together...\n"
        
        children = raw_input("Are you going to have kids?"+ ENTRY_ARROW).lower()
        
        check = CheckEntry(self.children_options)  
        acceptable_entry, next_decision, statement = check.acceptable(children)
               
        if acceptable_entry is False:  
                          
            return check.new_attempt()
       
        else:    
            
            return next_decision, statement
            

class Family(object):
    
    def take(self):
        
        print LINE
        print "You chose to have kids, but the numbers of family mambers"
        print "also matters.\n"
        
        try:
        
            num_kids = int(raw_input("How many kids you have?" + ENTRY_ARROW))
            
            if num_kids == 1:
            
                return "health", "You had one kid."
                
            elif num_kids == 0:
            
                return "health", "You changed your mind, you didn't have any kid afterall."
                
            else:
            
                return "health", "You had %d kids." % (num_kids)
        
        except:
        
            print "You didn't enter a number... I guess you should not have kids."
            return "health", "You didn't handle well the idea of having kids. No kids."

    
class Health(object):
  
    def take(self):
        
        print LINE
        print "The way you treat your body is very important too. Try to make a weekly avarege of:\n"
                
        try:
        
            hours_sport = int(raw_input("How many hours of physical activities?"+ ENTRY_ARROW))       
            litres_alcohol = int(raw_input("How many liters of alcohol?"+ ENTRY_ARROW))
            cigarettes = int(raw_input("and how many cigarettes do you smoke? (enter '0' if none)"+ ENTRY_ARROW))
                
            if hours_sport == (litres_alcohol + cigarettes):
            
                return "happiness", "You had an average health routine - well balanced."
                
            elif hours_sport < (litres_alcohol + cigarettes):
            
                return "happiness", "You had a very bad health routine - smoked and drunk more then doing sports!"
                
            elif (hours_sport > 5) and (litres_alcohol + cigarettes == 0):
            
                return "happiness", "You had a pretty healthy lifestyle - no smoke, no alcohol and much exercise."
                
            else:
            
                return "happiness", "You had an ok health routine."

        except: 
            
            print "You didn't enter an integer number."
            print "I am afraid your sight is very bad."
            return "happiness", "You became probably blind... and this is not a joke!"
     
    
class Happiness(object):
    """Assuming a player doens't die before, this class is always the second to last. Before this class, the player summary is printed."""
    
    happiness_options = [("death", ["yes", "y", "sure", "of course", "obviously"], "Great! You are happy about your life."),
                         ("death", ["not sure", "maybe", "no", "n", "meh"], "You're not really happy about your life.")]
    
    def take(self):
        
        print LINE
        print "This above is the summary of your life."
        print "We could see your life as a process towards the pursue of happiness."
        print "Looking back at your life decisions,\n"

        happy = raw_input("Would you consider yourself happy?"+ ENTRY_ARROW).lower()
        
        check = CheckEntry(self.happiness_options)  
        acceptable_entry, next_decision, statement = check.acceptable(happy)
                    
        if acceptable_entry is False:
            
            next_decision, statement = check.new_attempt()
            
            print LINE
            print statement + "\n"            
            return next_decision, statement
           
        else:
        
            print LINE
            print statement + "\n"
            return next_decision, statement 
        
    
class Death(object):
    
    deaths = ["You die for lung cancer.",
              "You die alone in an nursery home.",
              "You have been shot by a stranger.",
              "You have a stroke.",
              "You have a heart attack while ascending the stairs.",
              "You die in a car accident in your 50s."]
                 
    def take(self):      
        
        print LINE
        print "At the end, there is only one certainty in your life..."
        print "\n\t\t\tYOUR DEATH:\n"        
        
        print self.deaths[randint(0,(len(self.deaths)-1))]
        
        print "\n\t\t\tTHE MORAL OF THE GAME:\n"
        print "It really doesn't matter what you choose to do in life as long as you"
        print "are happy... we all die randomly, afterall."
        
        print LINE
        exit("Goobye! Hope you learned something.")
            
    
class PlayDecisions(object):
            
                      
    def __init__(self, a_decision, a_summary):   
        self.a_game = a_decision
        self.player_summary = a_summary
        
    def play_game(self):
    
        current_decision = self.a_game.start_game()     # current_decision = Start() 
        
        while True:            
                 
            self.name_next_decision, self.statement = current_decision.take()      
            self.player_summary.add(self.statement)
            
            if self.name_next_decision == "happiness":
            
                print LINE
                self.player_summary.show()           
            
            current_decision = self.a_game.go_to_next_decision(self.name_next_decision) 
    
    
class LifeDecisions(object):

    list_decisions = {"start": Start(),
                      "university": University(),
                      "humble_job": HumbleJob(),
                      "rich": Rich(),
                      "unemployment": Unemployment(),
                      "love": Love(),
                      "children": Children(),
                      "family": Family(),
                      "health": Health(),
                      "happiness": Happiness(),
                      "death": Death()}
                          

    def __init__(self, start_decision):
        self.start_decision = start_decision
        
    def go_to_next_decision(self, next_decision):
        return self.list_decisions.get(next_decision)
     
    def start_game(self):
        return self.go_to_next_decision(self.start_decision)
        

######

a_start = LifeDecisions("start")
a_player = PlayerSummary()
a_game = PlayDecisions(a_start, a_player)
a_game.play_game()

