# A string with a numeric variable
x = "There are %d types of people." % 10
# Create a string
binary = "binary"
# Create a string
do_not = "don't"
# Create a string with embadded two strings
y = "Those who know %s and those who %s." % (binary, do_not)

# print a string with an embadded numeric variable
print x
# print a string with two embadded strings
print y

# print a string with a string
print "I said: %r." % x
# print a string with a string
print "I also said: '%s'." % y

# create a string called hilarious
hilarious = False
# create a string with an embadded variable/string
joke_evaluation = "Isn't that joke so funny? %r"

# print the string joke_evaluation with embadded variable the hilarious string
print joke_evaluation %hilarious

# create two text strings called 'w' and 'e'
w = "This is the left side of ..."
e = "a string with a right side."

# print two srings 'w' and 'e'
print w + e
