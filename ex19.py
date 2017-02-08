# I use def for creating a function that print two virables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % (cheese_count)
    print "You have %d boxes of crackers!" % (boxes_of_crackers)
    print "Man that's enough for a party"
    print "Get a blanket.\n"

# I call the function with 20 and 30 as values for the arguments  
print "We can just give the functionn numbers directly:"
cheese_and_crackers(20,30)
    
# I create two variables in the scripts with their values    
print "OR, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

# I call those variables in the function arguments   
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
    
 # I call the function by using mathematical operations as argument   
print "We can even do math inside too: "
cheese_and_crackers(10+20, 5+6)
    
# I call the function combined the ways: calling the variable and adding mathematical  
print "And we can combine the two, variables and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Study drill section
def items_to_shop(number_items):
  if (number_items > 10):
    print "You cannot go to the express line, sorry"
  else:
    print "Go to the express line! Yuppy!"

items_to_shop(10)
items_to_shop(9+2)
num = 5
items_to_shop(num)
