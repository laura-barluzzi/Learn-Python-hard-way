import web
from gothonweb import map_game

urls = ( "/game", "GameEngine",
         "/", "Index" )

app = web.application(urls, globals())

#little hack

if web.config.get("_session") is None:
    store = web.session.DiskStore("sessions")
    session = web.session.Session(app, store, initializer={"room": None})
    web.config._session = session

else:
     session = web.config._session

render = web.template.render('templates/', base = "layout")

class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map_game.START
        web.seeother("/game")   # do research on seeother
        
class GameEngine(object):

    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        
    def POST(self):
        form = web.input(action = None)      
             
        if form.action in session.room.paths.keys():
            session.room = session.room.go(form.action)
            
        else:
            session.room = map_game.generic_death
            
        web.seeother("/game")      
        
if __name__ == "__main__":
    app.run()
