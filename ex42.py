## Anmal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self, name):
        self.name = name  
        print "It is an animal named %s" % self.name
        
## Dog is-an Animal
class Dog(Animal):
    
    def __init__(self, name, breed):
        ## Dog has-a name
        self.breed = breed
        super(Dog, self).__init__(name)
        print "it is also a dog of %s breed" % self.breed

Brittany = Dog("pussy", "Brittany")

      

## Cat is-an Animal
class Cat(Animal):
    
    def __init__(self, name):
        super(Cat, self).__init__(name)
        print "it is a cat"

Catty = Cat("Catty")



## Person is-an Object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
        print "%s is a person" % (name)
        
## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## Employee has-a name inherited from class Person
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        print "and makes %d money" % self.salary
        
Clemens = Employee("Clemens", 90000)
Clemens.pet = Brittany
print Clemens.pet

       
## Fish is-an object
class Fish(object):
    
    def __init__(self, name):
        self.name = name
        print "The name of the Fish is: %s" % name
     
## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, name, origin):
      self.origin = origin
      super(Salmon, self).__init__(name)
      print "it comes from the %s" % self.origin

Sockey = Salmon("sockey", "pacific ocean")

           
## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self, name):
        super(Halibut, self).__init__(name)
        print "and it's not as tasty as salmon"


## rover is-a dog
rover = Dog("Rover", "Akita")

## satan is-a cat
satan = Cat("Satan")

## Mary is-a Person and has-a name Mary
mary = Person("Mary")

## Mary has-a pet (inherited from class Person as Mary is-a Person)
mary.pet = satan

## Frank is-an Employee and has-a salary
frank = Employee("Frank", 120000)

## Frank has-a pet
frank.pet = rover

## Flipper is-a Fish
flipper = Fish("Flipper")

## Crouse is-a Salmon
crouse = Salmon("Crouse", "nordic oceans")

## Harry is-a Halibut
harry = Halibut("Harry")

