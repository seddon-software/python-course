import cherrypy
import json
#from cherrypy.process.plugins import Daemonizer

class Root(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        print(cherrypy.request.method)
        return u'It is me again at {0} with {1}'.format(args, kwargs)

    @cherrypy.expose
    def aaa(self):
        x = {'a':1,'b':2,'c':3}
        return json.dumps(x)
    
    @cherrypy.expose
    def bbb(self, x, y):
        return x + y
    
    @cherrypy.expose
    def chris(self):
        response = cherrypy.response
 
        try:
            fileName="chris.txt"
            f = open(fileName, "r", encoding="UTF-8")
            data = f.read()
            return data
#             content = "abc"  #.encode()
#             response.body = content   #data.encode()
#             response.status = 200
#             response.headers['Content-type'] = "text/html" 
#             response.headers['Content-Length'] = str(len(content)) 
        except:
            print("oops")
     
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def abc(self):
        return "Goodbye Universe"

    @cherrypy.expose
    def xyz(self):
        return "Beware the ides of March"

if __name__ == '__main__':
#     d = Daemonizer(cherrypy.engine)
#     d.subscribe()
    cherrypy.config.update({'server.socket_port': 5050})
    cherrypy.server.socket_host = 'localhost'
    cherrypy.quickstart(Root(), '/')
    
