#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: import from seperate file, both main script and the test script (with global vars etc.)
import json

from email_client import SMTPClient
from tcp_client import TCPClient
from helpers import read_latest_report

TESTS = [
    'tests/test1.json',
    'tests/test2.json',
    'tests/test3.json',
    'tests/test4.json'
]

def main():
    mail_client = SMTPClient()
    tcp_client = TCPClient()

    # Run tests
    for test in TESTS:
        # Get test data
        with open(test, 'r') as test_file:
            test_service = json.load(test_file)
            read_latest_report(test_service, mail_client, tcp_client)

    # Write test report..

if __name__ == "__main__":
	main()
