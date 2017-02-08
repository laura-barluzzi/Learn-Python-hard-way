# like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# that args is pointless, we can do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# takes just one argument
def print_one(arg1):
    print "arg2: %r" % (arg1)
    
# this takes no argument
def print_none():
    print "I got nothing"


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
