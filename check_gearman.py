#!/usr/bin/python
# -*- coding: utf-8 -*-

import gearman
import json
import sys
import argparse


def discover_tasks(server, port):
    d = {'data': []}
    gm_admin_client = gearman.GearmanAdminClient(
        [':'.join([server, str(port)])])
    for task in gm_admin_client.get_status():
        d['data'].append({'{#TASK}': task['task']})
    return json.dumps(d)


def get_task_info(server, port, function, task_name):
    gm_admin_client = gearman.GearmanAdminClient(
        [':'.join([server, str(port)])])
    if function == 'jobs':
        for task in gm_admin_client.get_status():
            if task['task'] == task_name:
                print task['queued']
    elif function == 'workers':
        for task in gm_admin_client.get_status():
            if task['task'] == task_name:
                print task['workers']


if __name__ == '__main__':
    server = sys.argv[1]
    port = sys.argv[2]
    api = sys.argv[3]
    function = sys.argv[4]
    task_name = sys.argv[5]

    arg_parser = argparse.ArgumentParser(
        description='Gearman check for Zabbix')
    arg_parser.add_argument(
        '-H', '--host', help="Specify host or ip address", default="localhost",
        required=True)
    arg_parser.add_argument(
        '-p', '--port', help="Specify port - default 4730", type=int,
        default=4730)
    arg_parser.add_argument(
        '-a', '--api', help="Specify api - [discover, stat]",
        required=True)
    arg_parser.add_argument(
        '-f', '--function', help="Specify stat function - [jobs, workers]")
    arg_parser.add_argument('-t', '--task', help="Specify task's name")
    arguments = arg_parser.parse_args()

    if arguments.api == 'discover':
        print discover_tasks(arguments.host, arguments.port)
    elif arguments.api == 'stat':
        get_task_info(
            arguments.host, arguments.port, arguments.function, arguments.task)
