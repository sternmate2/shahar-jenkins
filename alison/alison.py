from .alison_logger import logger
from .listeners import TCPListener, UDPListener
from prometheus_client import start_http_server

class Alison:
    def __init__(self, addr='0.0.0.0', port=8888):
        self.addr = addr
        self.port = port
        logger.info(f'Alison started')

    def start_tcp(self):
        self.tcp_instance = TCPListener(self.addr, self.port)
        self.tcp_instance.start()
        logger.info(f'Listening on {self.addr}:{self.port} TCP')

    def start_udp(self):
        self.udp_instance = UDPListener(self.addr, self.port)
        self.udp_instance.start()
        logger.info(f'Listening on {self.addr}:{self.port} UDP')

    def stop_udp(self):
        self.udp_instance.stop()
        logger.info('Stopped Alison UDP listener')

    def stop_tcp(self):
        self.tcp_instance.stop()
        logger.info('Stopped Alison TCP listener')
