from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This is only to have a superclass"
        exit(1)

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()  # self.scene_map is a_map that is Map('central_corridor'). It's a Map object so we apply the method opening_scene() that is part of class Map. 
        print "THE CURRENT SCENE IS: ", current_scene
        
        while True:
            print "\n-------------"
            next_scene_name = current_scene.enter() # next_scene_name takes the returned value from enter() in the current scene
            current_scene = self.scene_map.next_scene(next_scene_name)
            
class Death(Scene):

    list_deaths = ["You died. You kinda suck at this.", 
                   "Your mom would be proud... if she were smarter.", 
                   "Such a luser.",
                   "I have a small puppy that's better at this."]
                   
    def enter(self):
        print Death.list_deaths[randint(0, len(self.list_deaths)-1)]    # randomly pick up the index and print the content at that index
        exit(1)
            
class CentralCorridor(Scene):
    
    def enter(self):
        print """
The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
You are the last surviving member and your last mission is to get the neutron desruct 
bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting 
into an escape pod.

You're running down the central corridor to the Weapons Armory when a Gothon jumps out, 
red scaly skin, dark grimy teeth, and evil clow costume flowing around his hate filled 
body. He's blocking the door to the Armory and about to pull a weapon to blast you."""

        action = raw_input("What do you do? --> ")

        if action == "shoot!":
            print """
Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume 
is flowing and moving around his body, which throws off your aim. Your laser hits his 
costume but misses him entirely. This completely ruins his brand new costume his mother 
bought him, which makes him fly into a rage and blast you repeatedly in the face until 
you are dead. Then he eats you. """
            return 'death'
            
        elif action == "dodge!":
            print """
Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you"""
            return 'death'

        elif action == "tell a joke":
            print """
Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon 
joke you know: 
\"Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvff ddifjdiji.\"
While he's laughing you run up and shoot him square in the head putting him down, 
then jump through the Weapon Armory door."""
            return 'laser_weapon_armory'

        else: 
            print "Does not compute!"
            return 'central_corridor'
    
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print """
You do a dive roll into the Weapon Armory, crouch and sca the room for more Gothons that 
might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the 
rooom and find the neutron bomb in its container. There's a keypad lock on the box and 
you need the code to get the bomb out. If you get the code wrong 10 times then the lock 
closes foreever and you cannot get the bomb. The code is 3 digits"""

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) 
        guess = raw_input("Guess the 3-digit code --> ")
        guesses = 1
        
        while code != guess and guesses < 10:          
            guess = raw_input("INVALIDE! \nOnly %d attempts left --> " % (10-guesses))
            guesses += 1
            
        if code == guess: 
            print """
The container clicks open and hte seal breaks, letting gas out. You grab the neutron bomb 
and run as fast as you can to the bridge where you must place it in the right spot."""
            return 'the_bridge'
        
        else: 
            print """
The lock buzzzes one last time and then you hera a sickening melting sound as the mechanism 
is fused together. You decide to sit there, and ifinally the Gothons blow up the ship from 
their ship and you die"""
            return 'death'  
            
class TheBridge(Scene):
    
    def enter(self):
        print """
You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 
Gothons who are trying to take control of the ship. Each of them has an even uglier clown 
costume than the last. Tehy haven't pulled their weapons out yet, as they see the active 
bomb under your arm and don't want ot set it off."""

        action = raw_input("What do you do? --> ")
        
        if action == "throw the bomb":
            print """
In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right 
as you drop it a Gothon shoots you right in the back killing you. As you die you see another 
Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when 
it goes off."""
            return 'death'
            
        elif action == "slowly palce the bomb":
            print """
You point our blaster at the bomb under your arm and the Gothons put their hands up and start 
to sweat. You inch backward to the door, open it, and then carefully place the bomb on the 
floor, pinting your blaster at it. You tehn jump back through the door, punch the close button 
and blast the lock so the Gothons cannot get out. Now that the bomb is placed you run to the 
escape pod to get off this tin can."""
            return 'escape_pod'
            
        else: 
            print "DOES NOT COMPUTE"
            return 'the_bridge'   
            
class EscapePod(Scene):
    
    def enter(self):
        print """
You rush through the ship desperately trying to make it to the escape pod before the whole ship 
explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. 
You get to the chamber with the escape pods, and now need to pick one to take. Some of them could 
be damaged but you don't have time to look. There are 5 pods, which one do you take?"""
        
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            print """
You jump into pod %s and hit the eject button. The pod escapes out into the void of space, then 
implodes as the hull ruptures, crushing your body into jam jelly.""" % (guess)
            return 'death'
            
        else: 
            print """
You jump into pod %s and hit the eject button. The pod easily slides out into space heading to the 
planet below. As it flies to the planet, you look back and see your ship implode then explode like 
a bright star, taking out the Gothon ship at the same tiime. You won!""" 
            return 'finished'   
            
class Map(object): 
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(), 
        'escape_pod': EscapePod(),
        'death': Death()}
        
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)  
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
        
