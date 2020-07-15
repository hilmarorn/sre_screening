#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from email_client import SMTPClient
from tcp_client import TCPClient
from helpers import read_latest_report

TESTS = [
    {
        'id': '1',
        'input': 'tests/test1.json',
        'send_email': False,
        'send_tcp': False
    },
    {
        'id': '2',
        'input': 'tests/test2.json',
        'send_email': True,
        'send_tcp': True
    },
    {
        'id': '3',
        'input': 'tests/test3.json',
        'send_email': False,
        'send_tcp': True
    },
    {
        'id': '4',
        'input': 'tests/test4.json',
        'send_email': True,
        'send_tcp': False
    }
]

def main():
    mail_client = SMTPClient()
    tcp_client = TCPClient()

    for test in TESTS:
        # Get test data
        with open(test['input'], 'r') as test_file:
            test_service = json.load(test_file)
            sent_email, sent_tcp = read_latest_report(test_service, mail_client, tcp_client)

            # Run tests
            if test['send_email'] != sent_email or test['send_tcp'] != sent_tcp:
                print('Test %s failed!' % test['id'])
                quit()
        
    print('All %s tests were success!' % len(TESTS))

if __name__ == "__main__":
	main()
