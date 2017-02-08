

class PlayerSummary(object):
    """This class is imported in the ex45_game.py to build and print a player life summary."""
    
    life_summary = ["\n\t\t\tYOUR LIFE IN FEW LINES:\n"]
        
    def add(self, current_statement):
        self.life_summary.append(current_statement)
    
    def show(self):
        for decision in self.life_summary:
            print decision
