numbers = []

# while-loop study drill
i = 0
list_capacity = 6

def create_number_list(i, i_increase, list_capacity):
    while i < list_capacity:
        print "At the top i is %d" % (i)
        numbers.append(i)
    
        i += i_increase
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % (i)
        
create_number_list(0, 2, int(raw_input("What's the total number of elements in your list?: ")))
   
print "The numbers: "

for num in numbers: 
    print num
    
    
# same with for-loops and no change in increment 
def create_number_list(i, i_increase, list_capacity):
    for i in range(0, list_capacity):
        print "At the top i is %d" % (i)
        numbers.append(i)
        i += 2    # this i become 2 but then when it restart for-loop reset 
        print i
 
create_number_list(0, 2, int(raw_input("What's the total number of elements in your list?: ")))
   
print "The numbers: "

for num in numbers: 
    print num
    
    
# other example with while-loop
colors = []

def create_list_of_colors(number_elements, step):
    i = 0
    while i < number_elements:        
        colors.append(raw_input("Type a new color: "))
        i += step
        print i
                
create_list_of_colors(10,2)

for color in colors:
    print color
