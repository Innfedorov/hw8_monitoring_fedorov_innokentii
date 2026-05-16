from prometheus_client import start_http_server, Histogram
import time
import random

REQUEST_TIME = Histogram('request_processing_seconds', 'Time spent processing request')

def process_request():
    with REQUEST_TIME.time():
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == '__main__':
    start_http_server(8000)
    print("ML Service running on port 8000")
    while True:
        process_request()
        time.sleep(1)
