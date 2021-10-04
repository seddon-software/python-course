import cherrypy
import json
#from cherrypy.process.plugins import Daemonizer

class Root(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        print(kwargs)
        print(cherrypy.request.method)
        return f'PATH = {args} with {kwargs}'

    @cherrypy.expose
    def abc_parameters(self):
        x = {'a':1,'b':2,'c':3}
        return json.dumps(x)
    
    @cherrypy.expose
    def sum(self, x, y):
        return f"{float(x) + float(y)}"
    
    @cherrypy.expose
    def chris(self):
        response = cherrypy.response
 
        try:
            fileName="chris.txt"
            f = open(fileName, "r", encoding="UTF-8")
            data = f.read()
            return data
        except:
            print("oops")
     
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def goodbye(self):
        return "Goodbye Universe"

    @cherrypy.expose
    def ides(self):
        return "Beware the ides of March"

if __name__ == '__main__':
#     d = Daemonizer(cherrypy.engine)
#     d.subscribe()
    cherrypy.config.update({'server.socket_port': 5050})
    cherrypy.server.socket_host = 'localhost'
    cherrypy.quickstart(Root(), '/')
    
