from flask import Flask
from healthcheck import HealthCheck
from .alison_logger import logger
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

HEALTH_PORT = 5000
HEALTH_ENDPOINT = '/health'


def health_check():
    return True, "Alison ok"

def start_monitoring():
    app = Flask(__name__)
    health = HealthCheck()
    # health = HealthCheck(app, "/health")
    health.add_check(health_check)
    app.add_url_rule(HEALTH_ENDPOINT, "healthcheck", view_func=lambda: health.run())
    # app.run()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(HEALTH_PORT)
    logger.info(f'healthCheck on http://localhost:{HEALTH_PORT}{HEALTH_ENDPOINT}')
    IOLoop.instance().start()
