import image_processor
import data_processor
import font_generator
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Contenxt-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()
 #Handler for the GET requests
    def do_GET(self):
        self._set_headers()
        # Send the html message
        self.wfile.write(json.dumps({'hello':'world'}).encode('ascii'))
        return

    def do_POST(self):
           
        # read the message and convert it into a python dictionary
        # length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read())
        
        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))
        
	#Create a web server and define the handler to manage the
	#incoming request
def run(server_class=HTTPServer, handler_class=Server, port=8008):
   server_address = ('', port)
   httpd = server_class(server_address, handler_class)
   print( 'Starting httpd on port %d...', port)
   httpd.serve_forever()


def main(dir):
    dirname = dir
    i = 0
    while os.path.exists('my_fonts/'+dirname):
        dirname = dir + '-' + str(i)
        i += 1
    print('Processing image source ...')
    image_processor.cropImages('src/images/'+dir+'.jpg', dirname)
    print('Building data objects ...')
    data_processor.setGlyphs(dirname)
    print('Configuring custom font ...')
    font_generator.configFont('font.json', dir)

if __name__ == '__main__':
    print('Hand Spoken 1.0; PennApps Fall 2019. Making the art of handwriting accessible, one voice at a time.')
    print('Dryden, Jennifer\tCui, Kevin\nXu, Stephanie\t\tZhang, Alex')
    print('Launching Hand Spoken ...')
    main('text-jennifer')
    print('Process success!')
    run()