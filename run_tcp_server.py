#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver

HOST, PORT = "127.0.0.1", 5005

class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    
    https://docs.python.org/3.6/library/socketserver.html#examples

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    # Activate the server; this will keep running until you interrupt the program with Ctrl-C
    server.serve_forever()
