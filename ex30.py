people = 30 
cars = 20
buses = 15

if cars > people: 
    print "We should take the cars."
elif cars < people: 
    print "We should not take the cars."
else: 
    print "We can't decide."
    
if buses > cars: 
    print "That's too many buses."
elif buses < cars: 
    print "Maybe we could take the buses."
else: 
    print "We still can't decide."
    
if people > buses: 
    print "Alright, let's just take the buses."
else: 
    print "Fine, let's stay home then."

# study drill    
if (buses < cars < people): 
    print "We need more buses!"

# other usage
user_age = int(raw_input("What's your age?: "))

if user_age < 13: 
    print "You are child: you should go out and play."
elif 13 <= user_age < 20:
    print "You are a teen! Don't drive your parents too crazy."
elif 20 <= user_age < 40:
    print "Young adult... in other words: tough decisions!"
elif 40 <= user_age < 60:
    print "Middle age crisis? Remember that regretting is useless!"
else: 
    print "You are old.. be wise not crumpy!"
