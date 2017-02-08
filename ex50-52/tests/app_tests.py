from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    
    # check that we get a 404 on the /hello URL
    resp = app.request("/hello")
    assert_response(resp, status="404")
    
    # test our first GET request to /
    resp = app.request("/")
    assert_response(resp, status="303")
    
def test_game_engine():

    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)    
    
    # make sure default value for action is None
    resp = app.request("/game", method="POST")
    assert_response(resp, contains=None, status="303")

    # test that we get expected values
    data = {"action": "tell a joke"}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, contains=None, status="303")
