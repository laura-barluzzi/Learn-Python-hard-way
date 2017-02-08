# in the shell you can do help("ex25") to see all the function """comments"""
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # from a string creates a list of items separated by ' ' 
    return words
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words) 

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)  # remove a word in a string (here the first)
    print word

def print_last_word(words):
    """Prints the last word after poppoing it off."""
    word = words.pop(-1) # remove a word, the last one in this case
    print word

def sort_sentenece(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
