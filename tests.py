import dns.resolver
import unittest
from alison.alison import Alison
import gevent
import threading


HOST, PORT = '127.0.0.1', 8888


class AlisonThread(threading.Thread):
    def __init__(self,  *args, **kwargs):
        super(AlisonThread, self).__init__(*args, **kwargs)
        self.alison = Alison()
        # self._stop_event = self.alison.stop_udp
        self._stop_event = threading.Event()

    def run(self):
        self.alison.start_udp()
        gevent.wait(timeout=3)


    def stop(self):
        self.alison.stop_udp()
        self._stop_event.set()


class testAlison(unittest.TestCase):
    def test_dns_query(self):
        res = dns.resolver.Resolver(configure=False)
        # res.lifetime = res.timeout = 5
        res.nameservers = [HOST]
        res.port = PORT
        dns_answer = res.query('1dot1dot1dot1.cloudflare-dns.com', 'a')
        result = '1.1.1.1' in [ip.to_text() for ip in dns_answer]
        self.assertEqual(result, True)

if __name__ == '__main__':
    alison_thread = AlisonThread()
    alison_thread.deamon = True
    alison_thread.start()
    unittest.main()
    # alison_thread.stop()
