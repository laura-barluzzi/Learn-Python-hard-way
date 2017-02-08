# make a list 
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for-loop that goes through a list
for number in the_count: 
    print "This is count %d" % (number)

for fruit in fruits: 
    print "A fruit of type: %s" % (fruit)
    
# we can build lists with for-loops
elements = []
for i in range(1, 7):  # 1-6 included, 7 is excluded
    print "Additing %d to the list." % (i)
    # append is a funciton that lists understand
    elements.append(i)

for i in elements: 
    print "Element was: %d" % (i)
    
