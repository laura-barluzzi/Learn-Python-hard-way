ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')   # creates a list from string
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana" , "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # it starts from the end of the list
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)   # create a string joining all elements of the list by separating them with ' ' - opposite of .split
print '#'.join(stuff[3:5])  # create a string by joining the two elements (index 3 and 4), separating them with a #
