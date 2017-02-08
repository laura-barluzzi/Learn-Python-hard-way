#  Override Explicitly

class Parent(object):
    
    def override(self):
        print "PARENT override()"
        
class Child(Parent):
    
    def override(self):
        print "CHILD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()

# alter before or after using SUPER()

class Parent(object):


    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):
    
    def altered(self):
        print "CHILD, before PARENT altered()"
        super(Child, self).altered()    # directly call altered in super class Parent
        print "CHILD, after PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

# composition

class Other(object):

    
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        
class Child(object):

    
    def __init__(self):
        self.other = Other()    # in Child I create a variable equal to an object of Other() so I can use all Other() methods on self.other
        
    def implicit(self):
        self.other.implicit()   # indeed, here an example
        
    def override(self):
        print "CHILD override()"
        
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()
