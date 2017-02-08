# Asking questions
print "How old are you?", # the comma allows the next line to appear next to this one
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# other options for raw_input()

age = raw_input("How old are you? ")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So, you're %r old, %r tall and %r heavy."  %  (age,  height,  weight)

# Another option I write

funny = raw_input("Do you consider yourself funny?")
confident = raw_input("How confident are you about being funny in a range 1-5? 5 = very confident")
print "So, you considered yourself %s and you are %s confident in saying so" % (funny, confident)

# How old are you and input no integer variables
age = raw_input("How old are you? ")
print age

# with integer variables that accepts only entire numeric values
age1 = int(raw_input("How old are you? "))
print age1
