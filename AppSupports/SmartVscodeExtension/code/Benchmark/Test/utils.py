import requests
import json
import threading
import queue

from AppSupports.SmartVscodeExtension.code.Benchmark.Test.TaskTestResult import TaskTestResult

import configparser
parser = configparser.ConfigParser()
parser.read("config.ini")
FRONTEND_SERVER_HOST = "localhost"
FRONTEND_SERVER_PORT = int(parser.get('Server', 'TEST_SERVER_PORT'))
TEST_CLIENT_PORT = int(parser.get('Server', 'TEST_CLIENT_PORT'))



def send_test_case(case):
    requests.post(f"http://{FRONTEND_SERVER_HOST}:{FRONTEND_SERVER_PORT}/test_mode", data=json.dumps(case))


from http.server import BaseHTTPRequestHandler, HTTPServer

data_queue = queue.Queue()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            json_data = json.loads(post_data)
            # print("receive data", json_data)
            data_queue.put(json_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "success"}
            self.wfile.write(json.dumps(response).encode())

        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()


def run_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=TEST_CLIENT_PORT):
    global httpd
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def spawn_server_thread():
    global server_thread
    server_thread = threading.Thread(target=run_server, kwargs={"port": TEST_CLIENT_PORT})
    # server_thread.daemon = True
    server_thread.start()

def stop_server():
    if 'httpd' in globals():
        httpd.shutdown()
        httpd.server_close()
    # httpd = http_queue.get(block=True)
    # httpd.shutdown()
    # httpd.server_close()
    if 'server_thread' in globals():
        server_thread.join()



def receive_test_result():
    data = data_queue.get(block=True)
    return TaskTestResult(data["success"], data["info"])


def test_one_case(case: dict):
    send_test_case(case)
    res = receive_test_result()
    print("Success: ", res.success)
    print("Info: ", res.info)
    return res
