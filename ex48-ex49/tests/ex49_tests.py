from nose.tools import *
from ex48 import ex49
from ex48.ex49 import ParserError

empty_list = []

    
def test_sentence_object():
    
    a_sentence = ex49.Sentence(("noun", "player"),("verb", "enter"), ("noun", "door"))
    
    assert_equal(a_sentence.subject, "player")
    assert_equal(a_sentence.verb, "enter")
    assert_equal(a_sentence.obj, "door")
    
def test_peek():
    test_list = [("noun", "bear"), ("verb", "go"), ("stop", "the")]         
           
    assert_equal(ex49.peek(test_list), "noun")
    assert_equal(ex49.peek(empty_list), None)

def test_match():        
    
    assert_equal(ex49.match([("noun", "bear"), ("verb", "go"), ("stop", "the")], "stop"), None)
    assert_equal(ex49.match([("noun", "bear"), ("verb", "go"), ("stop", "the")], "noun"), ("noun", "bear"))
    assert_equal(ex49.match([("verb", "go"), ("stop", "the"), ("noun", "bear")], "verb"), ("verb", "go"))
    assert_equal(ex49.match(empty_list, "noun"), None)

def test_skip():
    test_list = [("stop", "the"), ("noun", "bear"), ("verb", "go")]
    test_list2 = [("stop", "in"), ("stop", "the"), ("noun", "bear"), ("verb", "go")]
   
    ex49.skip(test_list, "stop")
    assert_equal(test_list, [("noun", "bear"), ("verb", "go")])    
    
    ex49.skip(test_list2, "stop")    
    assert_equal(test_list2, [("noun", "bear"), ("verb", "go")])

def test_parse_verb():
    test_list = [("verb", "go"), ("direction", "south"), ("noun", "bear")]
    
    assert_equal(ex49.parse_verb(test_list), ("verb", "go"))
    
    #add error check
    
def test_parse_object():
    test_list1 = [("noun", "bear"), ("direction", "south")]
    test_list2 = [("direction", "south"), ("noun", "bear")]
    
    assert_equal(ex49.parse_object(test_list1), ("noun", "bear"))
    assert_equal(ex49.parse_object(test_list2), ("direction", "south"))
    # add assert_diverse - error
    
def test_parse_subject():
    
    test_list = [("verb", "enter"), ("noun", "door")]
    subj = ("noun", "player")
    
    a_sentence = ex49.parse_subject(test_list, subj)
    
    assert_equal(a_sentence.subject, "player")
    assert_equal(a_sentence.verb, "enter")
    assert_equal(a_sentence.obj, "door")
    
def test_parse_sentence():
    test_list1 = [("noun", "princess"), ("verb", "enter"), ("noun", "door")]
    test_list2 = [("verb", "hit"), ("noun", "bear")]
    
    parsed_sentence = ex49.parse_sentence(test_list1)   
    
    assert_equal(parsed_sentence.subject, "princess"),
    assert_equal(parsed_sentence.verb, "enter"),
    assert_equal(parsed_sentence.obj, "door")

    parsed_sentence2 = ex49.parse_sentence(test_list2)
                                
    assert_equal(parsed_sentence2.subject, "player"),
    assert_equal(parsed_sentence2.verb, "hit"),
    assert_equal(parsed_sentence2.obj, "bear")    

def test_raise_errors():
    
    
    test_list1 = [("direction", "north"), ("verb", "go"), ("noun", "princess")]
    test_list2 = [("noun", "princess"), ("verb", "go")]
    
    assert_raises(ParserError, ex49.parse_sentence, test_list1)
    #assert_raises(ParseError, parse_sentence, empty_list)
    
    assert_raises(ParserError, ex49.parse_verb, test_list1)
    assert_raises(ParserError, ex49.parse_verb, test_list2)
    #assert_raises(ParseError, parse_sentence, empty_list)
    
    assert_raises(ParserError, ex49.parse_object, [("verb", "go"), ("noun", "bear")])

    
