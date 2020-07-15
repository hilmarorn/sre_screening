#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

class TCPClient(object):

    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 5006

    def send_tcp_message(self, data):
        print('Sending tcp message to client {} with data {}'.format(self.HOST, data))
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((self.HOST, self.PORT))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
