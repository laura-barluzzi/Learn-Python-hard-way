name = 'Zed A. Shaw'
age = 35
height_in = 74 # inches
weight_lbs = 180 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

weight_kg = weight_lbs * 0.45
height_cm = height_in * 2.54

print "let's talk about %s." % name
print "He's %d inches and %d cm tall." % (height_in, height_cm)
print "He's %d pounds and %d kg heavy." % (weight_lbs, weight_kg)
print "actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky and I should get familiar with it
print "if I add %d, %d, and %d I get %d." % (age, height_in, weight_lbs, age + weight_lbs + height_in)
