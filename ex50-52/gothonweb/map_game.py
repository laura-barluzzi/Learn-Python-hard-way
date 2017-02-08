from sys import exit
from random import randint

GENERIC_DEATHS = ["You died. You kinda suck at this.", 
                 "Your mom would be proud... if she were smarter.", 
                 "Such a luser.",
                 "I have a small puppy that's better at this."]

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def generic_death_exit():
        if self.name == "death":
            exit(1)
        
    def go(self, direction):
        if self.paths:
            return self.paths.get(direction, "No key found in paths dictionary.")
        else:
            exit(1)
            
    def add_paths(self, paths):
        self.paths.update(paths)

# create rooms 
        
central_corridor = Room("Central Corridor", 
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
You are the last surviving member and your last mission is to get the neutron desruct 
bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting 
into an escape pod.

You're running down the central corridor to the Weapons Armory when a Gothon jumps out, 
red scaly skin, dark grimy teeth, and evil clow costume flowing around his hate filled 
body. He's blocking the door to the Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory", 
"""
Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon 
joke you know: 
\"Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvff ddifjdiji.\"
While he's laughing you run up and shoot him square in the head putting him down, 
then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and sca the room for more Gothons that 
might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of the 
rooom and find the neutron bomb in its container. There's a keypad lock on the box and 
you need the code to get the bomb out. If you get the code wrong 10 times then the lock 
closes foreever and you cannot get the bomb. The code is 3 digits.
""")

the_bridge = Room("The Bridge", 
"""
The container clicks open and hte seal breaks, letting gas out. You grab the neutron bomb 
and run as fast as you can to the bridge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 
Gothons who are trying to take control of the ship. Each of them has an even uglier clown 
costume than the last. Tehy haven't pulled their weapons out yet, as they see the active 
bomb under your arm and don't want ot set it off.
""")

escape_pod = Room("Escape Pod", 
"""
You point our blaster at the bomb under your arm and the Gothons put their hands up and start 
to sweat. You inch backward to the door, open it, and then carefully place the bomb on the 
floor, pinting your blaster at it. You tehn jump back through the door, punch the close button 
and blast the lock so the Gothons cannot get out. Now that the bomb is placed you run to the 
escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape pod before the whole ship 
explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. 
You get to the chamber with the escape pods, and now need to pick one to take. Some of them could 
be damaged but you don't have time to look. There are 5 pods, which one do you take?
""") 

the_end_winner = Room("The end", 
"""
You jump into pod 2 and hit the eject button. The pod easily slides out into space heading to the 
planet below. As it flies to the planet, you look back and see your ship implode then explode like 
a bright star, taking out the Gothon ship at the same time. You won!
""")

the_end_loser = Room("The end", 
"""
You jump into a random pod and hit the eject button. The pod escapes out into the void of space, then 
implodes as the hull ruptures, crushing your body into jam jelly.
""")

generic_death = Room("death", GENERIC_DEATHS[randint(0, len(GENERIC_DEATHS)-1)])

# add following paths per each room

escape_pod.add_paths({"2": the_end_winner,
                      "*": the_end_loser})

the_bridge.add_paths({"throw the bomb": generic_death,
                      "slowly place the bomb": escape_pod})
                      
laser_weapon_armory.add_paths({"0123": the_bridge,
                               "*": generic_death})
                               
central_corridor.add_paths({"shoot!": generic_death,
                            "dodge!": generic_death, 
                            "tell a joke": laser_weapon_armory})
                            
START = central_corridor
