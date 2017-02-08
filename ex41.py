import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):" : "Make a class named %%% that is-a %%%.", 
    "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.", 
    "class %%%(object):\n\tdef ***(self, @@@)" : "class %%% has-a function named *** that takes self and @@@ parameters.", 
    "*** = %%%()" : "Set *** to an instance fo class %%%", 
    "***.***(@@@)" : "From *** get the *** function, and call it with paramters self, @@@.",
    "***.*** = '***'" : "From *** get the *** attribute and set it to '***'."
    }
       
# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":     # len(sys.argv) == 1
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():  # f(x) urlopen is called with WORD_URL as parameter and then the file is opened
    WORDS.append(word.strip())  # I take the empty list WORDS and I call a method that add (append) a copy of the string 'word' (.strip())
    # at the end, WORDS = the whole text in the text file at the WORLD_URL

print WORDS 

   
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]  # random.sample(population, k) it returns a list with # a total number of elements equal to the amount of "%%%" found in snippets (which is PHRASES.keys(), wtih random elements from the WORDS list
     
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        # fake class names
        
        for word in class_names:
            result = result.replace("%%%", word, 1)
            
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # face parameter lists    
        for word in param_names: 
            result = result.replace("@@@", word, 1)

        results.append(result)
        
    return results
    
# keep going until they hit CTRL-D

try:
    while True:
        snippets = PHRASES.keys()   # I set snippets to a list of all the keys from dict PHRASES
        random.shuffle(snippets)    # I shuffle the list snippets
        
        for snippet in snippets:    # for each element of snippets
            phrase = PHRASES[snippet]   # set phrase to the value in PHRASES that is assigned to the key equal to the current snippet
            question, answer = convert(snippet, phrase) # set 2vars to the returns of the f(x) named convert with snippet, phrase parameter
            
            if PHRASE_FIRST:    # if this is true, covert the values of the 2 variable set before
                question, answer = answer, question
            
            print question
            
            raw_input("> Press CTRL-D to stop")
            print "ANSWER: %s\n\n" % (answer)

except EOFError:
    print "\nBye"        
