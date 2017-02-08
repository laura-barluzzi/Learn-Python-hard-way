

class CheckEntry(object):
    """takes a list of tuples with 3 items. The 1st item is the value of the next move; the 2nd item is a list of acceptable options for a specific user_entry; the 3rd item is a string to be added in a summary of the player game. Methods: acceptable(user_entry) allows to check if the entry is acceptable and it returns True/False and the respective 1st and 3rd items; new_attempt() allows the user to re-type once an entry and it returns 1st, 3rd items of acceptable entry or 'death', _"""

    def __init__(self, acceptable_options):
        
        self.acceptable_options = acceptable_options                
        self.acceptable_entry = False
        
    def acceptable(self, user_entry):      
        
        for next_move, option, statement in self.acceptable_options:
           
            if user_entry in option:                
                self.acceptable_entry = True
                break       
                         
        return self.acceptable_entry, next_move, statement
        
    def new_attempt(self):
            
        self.user_entry = raw_input("Ouch! It doesn't compute - type again your answer: ")            
        self.acceptable_entry, next_move, statement = self.acceptable(self.user_entry)
        
        if self.acceptable_entry == True:
        
            return next_move, statement
        
        else:
            
            return "death", "You don't deserve to play this game."              
