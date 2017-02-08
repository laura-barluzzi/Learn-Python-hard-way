# This code was copied-and-pasted from http://learnpythonthehardway.org/book/exercise26.txt
# This code was a mid-test to learn to read other people code and fix flaws

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
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
    
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# use of functions and printing

print "\nLet's practice everything."
print 'You\'d need to know about escapes with \'\\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\t\twhere there is none.
"""

print "--------------> \'A programmer poem\'"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %d" % (five)

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % (start_point)
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % (secret_formula(start_point))

sentence = "All good things come to those who wait."

words = break_words(sentence)
print "\nHere the list of words:\n", words, "\n"

sorted_words = sort_words(words)
print "Here the list of words sorted alphabetically:\n", sorted_words, "\n"

print "The first word is:" 
print_first_word(words)    # it prints a None
print "The last word is:"
print_last_word(words)  # it pritns a None

print "\n"
print_first_word(sorted_words)
print_last_word(sorted_words)

sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
