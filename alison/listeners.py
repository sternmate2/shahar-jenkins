from gevent.server import StreamServer,DatagramServer
from .client_context import ClientContextTCP,ClientContextUDP
from .alison_logger import logger


class TCPListener(StreamServer):
    def __init__(self, addr, port):
        super().__init__((addr, port))

    def handle(self, source, address):
        client = ClientContextTCP(source)
        client.serve_connection()

        # return result

class UDPListener(DatagramServer):
    def __init__(self, addr, port):
        super().__init__((addr, port))

    def handle(self, data, address):
        client = ClientContextUDP(self.socket, data, address)
        client.serve_connection()

        # return result