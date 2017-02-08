from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [("direction", "north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"), 
                          ("direction", "south"),
                          ("direction", "east")])
                          
def test_verbs():
    assert_equal(lexicon.scan("go"), [("verb", "go")])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [("verb", "go"), 
                          ("verb", "kill"),
                          ("verb", "eat")])
                          
def test_articles():
    assert_equal(lexicon.scan("the"), [("article", "the")])
    result = lexicon.scan("the an a")
    assert_equal(result, [("article", "the"), 
                          ("article", "an"),
                          ("article", "a")])
                          
def test_prepositions():
    assert_equal(lexicon.scan("on"), [("preposition", "on")])
    result = lexicon.scan("on at to")
    assert_equal(result, [("preposition", "on"), 
                          ("preposition", "at"),
                          ("preposition", "to")])                        

def test_nouns():
    assert_equal(lexicon.scan("bear"), [("noun", "bear")])
    result = lexicon.scan("bear princess")
    assert_equal(result, [("noun", "bear"),
                          ("noun", "princess")])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [("number", 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [("number", 3),
                          ("number", 91234)])
def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [("error", "ASDFADFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [("noun", "bear"),
                          ("error", "IAS"),
                          ("noun", "princess")])
                          
def test_capitalization():
    assert_equal(lexicon.scan("Bear"), [("noun", "Bear")])
    result = lexicon.scan("Bear IAS princess")
    assert_equal(result, [("noun", "Bear"),
                          ("error", "IAS"),
                          ("noun", "princess")])
