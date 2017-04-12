import threading
from http.server import BaseHTTPRequestHandler
from urllib import parse
import cgi
import argparse
from http.server import HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global queueList
        parsed_path = parse.urlparse(self.path)
        try:
            params = dict([p.split('=') for p in parsed_path[4].split('&')])
        except:
            params = {}
        queueNumber = int(params.get("queue"))
        if 0 <= queueNumber <= 10000:
            if len(queueList[int(params.get("queue"))]) > 0:
                message = queueList[int(params.get("queue"))][-1]
                del queueList[int(params.get("queue"))][-1]
                print(message)
            else:
                message = "Queue is empty"
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'json')
            self.end_headers()
            self.wfile.write(bytearray(message, 'utf8'))
        else:
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'json')
            self.end_headers()
            self.wfile.write(bytearray("Queue is out of index, it should be from 0 to 10000", 'utf8'))

    def do_POST(self):
        global queueList
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        queueNumber = int(form.getvalue("queue"))
        if 0 <= queueNumber <= 10000:
            queueList[queueNumber].append(form.getvalue("message"))
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'json')
            self.end_headers()
            self.wfile.write(bytearray(form.getvalue("message"), 'utf8'))
        else:
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'json')
            self.end_headers()
            self.wfile.write(bytearray("Queue is out of index, it should be from 0 to 10000", 'utf8'))


def start(port):
    global server
    global queueList
    queueList = [[] for i in range(10000)]
    server = HTTPServer(('localhost', port), Handler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    print('Starting server on ' + str(port) + ' port, use <Ctrl-C> to stop')


def stop():
    server.server_close()
    server.shutdown()


if __name__ == '__main__':
    global server
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action="store", dest="port", type=int, default=8080)
    args = parser.parse_args()
    start(args.port)
