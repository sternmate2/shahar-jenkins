import argparse
from .alison import Alison
from .monitoring import start_monitoring
import gevent
# from prometheus_client import start_http_server
ALISON_VERSION = "0.0.1"


def print_logo():
    header = "               _ _  \n"
    header += "         /\   | (_) VERSION %s\n" % ALISON_VERSION
    header += "        /  \  | |_ ___  ___  _ __ \n"
    header += "       / /\ \ | | / __|/ _ \| '_ \ \n"
    header += "      / ____ \| | \__ \ (_) | | | |  \n"
    header += "     /_/    \_\_|_|___/\___/|_| |_|  \n"
    header += "                   jonatanzafar59@gmail.com  \n"
    print(header)

def set_parser():
    parser = argparse.ArgumentParser(description='TCP/UPD proxy.')
    # proto_group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--tcp', action='store_true', help='TCP proxy')
    parser.add_argument('--udp', action='store_true', help='UDP proxy')
    # parser.add_argument('--tcp', required=True, help='Source IP and port, i.e.: 127.0.0.1:8000')
    # parser.add_argument('--udp', required=True, help='Destination IP and port, i.e.: 127.0.0.1:8888')
    args = parser.parse_args()
    return args

def main():
    args = set_parser()
    print_logo()
    alison = Alison()

    if args.tcp:
        alison.start_tcp()
    if args.udp:
        alison.start_udp()
    # start_monitoring()
    gevent.wait()


if __name__ == "__main__": 
    main()