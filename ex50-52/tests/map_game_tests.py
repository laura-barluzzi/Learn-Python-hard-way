from nose.tools import *
from gothonweb.map_game import *
from random import randint

def testroom():
    gold = Room("GoldRoom", 
                """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.description, """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.paths, {})
    
def test_room_paths():
    center = Room("CenterRoom", "Test room in the center.")
    north = Room("NorthRoom", "Test room in the north.")
    south = Room("SouthRoom", "Test room in the south.")
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)    

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    start.add_paths({"west": west, "down": down})
    west.add_paths({"east": start})
    down.add_paths({"up": start})
    
    assert_equal(start.go("west"), west)
    assert_equal(start.go("west").go("east"), start)
    assert_equal(start.go("down").go("up"), start)
    
def test_generic_death():
    list_deaths = ["My granma would be better at this.", "You are pathetic.", "Make yourself a favor, do something else."]
    random_index = randint(0, len(list_deaths)-1)
    generic_death = Room("Death", list_deaths[random_index])
    
    if random_index is 0:
        assert_equal(generic_death.description, "My granma would be better at this.")
        
    elif random_index is 1:
        assert_equal(generic_death.description, "You are pathetic.")
        
    else:
        assert_equal(generic_death.description, "Make yourself a favor, do something else.")  
    
    
def test_gothon_game_map():
    assert_equal(START.go("shoot!"), generic_death)
    assert_equal(START.go("dodge!"), generic_death)
    
    room = START.go("tell a joke")
    assert_equal(room, laser_weapon_armory)
    
"""
The crux of each test is a call to assertEqual() to check for an expected result; assertTrue() or assertFalse() to verify a condition; or assertRaises() to verify that a specific exception gets raised. 
"""
