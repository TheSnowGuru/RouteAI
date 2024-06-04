from prometheus_client import start_http_server, Summary
import time
from loguru import logger

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request():
    time.sleep(2)
    logger.info("Request processed")

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request()
