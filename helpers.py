#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

EVENT_LIMIT = 1000
ERROR_THRESHOLD = 0.1

def process_events(service, tcp_client):
    events = service['events']
    ok_events = events['ok'] if type(events['ok']) is int else int(events['ok'])
    error_events = events['error'] if type(events['error']) is int else int(events['error'])
    total_events = ok_events + error_events
    error_rate = error_events / total_events
    #print('Total events:', total_events, 'Error rate:', error_rate)
    
    if total_events >= EVENT_LIMIT and error_rate >= ERROR_THRESHOLD:
        error_precentage = '{}%'.format(int(error_rate * 100))
        tcp_message = 'Service id: {} -  Error rate: {}'.format(service['service_id'], error_precentage)
        tcp_client.send_tcp_message(tcp_message)

def read_latest_report(service, mail_client, tcp_client):
    if service['status'] and not service['status']['healthy']:
        mail_client.send_support_email(service)
    if service['events']:
        process_events(service, tcp_client)

def get_latest_events_json(current_events, service):
    if len(current_events) >= 1000:
        current_events = current_events[:1]
    return [service] + current_events

def write_events_report(service):
    latest_events_json = []
    with open('latest_events.json', 'r') as latest_file:
        loaded_json = json.load(latest_file)
        #print('Error json loaded:', loaded_json)
        latest_events_json = get_latest_events_json(loaded_json, service)
    
    with open("latest_events.json", "w") as outfile:
        #print('Write latest events json:', latest_events_json)
        json.dump(latest_events_json, outfile)
