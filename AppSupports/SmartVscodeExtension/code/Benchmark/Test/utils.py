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


class ThreadedHTTPServer:
    def __init__(self, host='localhost', port=5000):
        self.server = HTTPServer((host, port), SimpleHTTPRequestHandler)
        self.server_thread = None
        self.stop_event = threading.Event()

    def run_server(self):
        print("Starting server...")
        self.server.serve_forever()  # 使用 serve_forever() 来持续监听

    def start_server(self):
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def stop_server(self):
        print("Stopping server...")
        self.server.shutdown()  # 关闭HTTPServer
        self.server_thread.join()  # 等待线程结束
        print("Server thread has been joined.")



def receive_test_result():
    data = data_queue.get(block=True)
    return TaskTestResult(data["success"], data["info"])


def test_one_case(case: dict):
    send_test_case(case)
    res = receive_test_result()
    print("Success: ", res.success)
    print("Info: ", res.info)
    return res
