from sys import argv # import argv from python

script, recipe = argv # unpack arv into two arguments 

answer = '--> ' # create a string with '--> '

txt = open(recipe) 

print "The following delicious recipe is in the %s file:" % recipe

print " "
print txt.read() # print the whole text content of the file

print "Which other ingredient would you add?"
new_ingredient = raw_input(answer) 

print "\nThat sounds delicious! What's your name, co-cook?"
user_name = raw_input(answer) # create string user_name by terminal input 

print """
Great! So let's go cooking together, %s!
Let's use your suggested %s as new ingredient!
""" % (user_name, new_ingredient) # prints a text with two strings inside
