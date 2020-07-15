#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

from email_client import SMTPClient
from tcp_client import TCPClient
from helpers import read_latest_report, write_events_report

def main():
    mail_client = SMTPClient()
    tcp_client = TCPClient()

    input_json = sys.stdin.read()
    print('Raw input data:', input_json)
    service = json.loads(input_json)

    print('Report data:', service)
    sent_email, sent_tcp = read_latest_report(service, mail_client, tcp_client)
    write_events_report(service)

if __name__ == "__main__":
	main()
