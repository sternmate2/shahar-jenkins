import socket
import ssl
import struct
import dns.message
from .alison_logger import logger

HOST, PORT = '1.1.1.1', 853
class ClientContext:
    def __init__(self, client_socket):
        self.client_socket = client_socket
        # pass

    def validate_input(self, data):
        try:
            dns.message.from_wire(data)
        except Exception as e:
            logger.error('Input is not a valid DNS request')
            print(e)

    def serve_connection(self):
        data = self.receive_data()
        self.validate_input(data)
        upstream = Upstream()
        # data = self.toTCP(data)
        data = upstream.send_recv(data)
        # data = self.fromTCP(data)
        self.send_data(data)
        upstream.disconnect()

    def receive_data(self):
        raise NotImplementedError

    def send_data(self, data):
        raise NotImplementedError

class ClientContextTCP(ClientContext):

    def __init__(self, client_socket):
        super().__init__(client_socket)
        self.client_manager = AlisonTCPClient(self.client_socket)

    def receive_data(self):
        return self.client_manager.recv()

    def send_data(self, data):
        return self.client_manager.send(data)

class ClientContextUDP(ClientContext):

    def __init__(self, client_socket, data, address):
        super().__init__(client_socket)
        self.data = data
        self.client_socket = client_socket
        self.address = address

    def receive_data(self):
        return self.data

    def send_data(self, data):
        self.client_socket.sendto(data, self.address)

class Upstream:
    def __init__(self):
        self.client_session = self.create_session()
        self.connect()
        self.upstream_manager = AlisonTCPClient(self.wrappedSocket)


    def create_session(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(100)
        return sock

    def disconnect(self):
        self.wrappedSocket.close()

    def connect(self):
        self._wrap_session()
        try:
            # logger.debug("Connecting %r:%r" %(HOST, PORT))
            self.wrappedSocket.connect((HOST, PORT))
        except Exception as e:
            logger.error('Connection failed to %r:%r' %(HOST, PORT))

    def _wrap_session(self):
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_default_certs()
        self.wrappedSocket = context.wrap_socket(self.client_session, server_hostname=HOST)


    def send_recv(self, message):
        self.upstream_manager.send(message)
        response = self.upstream_manager.recv()
        logger.debug('finished DNS query')
        return response

class AlisonTCPClient():
    def __init__(self, client_socket):
        self.client_socket = client_socket

    def recv(self):
        try:
            length_field = self.client_socket.recv(2)
            payload_length, = struct.unpack('!H', length_field)
            return self.client_socket.recv(payload_length)
        except Exception as e:
            logger.error('Failed receiving response from server')
            print(e)

    def send(self, data):
        try:
            payload_length = len(data)
            data = struct.pack("!H", payload_length) + data
            self.client_socket.send(data)
        except Exception as e:
            logger.error('Failed sending message to server')
            print(e)