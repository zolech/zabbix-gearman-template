#!/usr/bin/python
import gearman
import json
import sys


def discover_tasks(server, port):
    d = {'data': []}
    gm_admin_client = gearman.GearmanAdminClient(
        [':'.join([server, str(port)])])
    for task in gm_admin_client.get_status():
        d['data'].append({'{#TASK}': task['task']})
    return json.dumps(d, indent=1) # delete indent

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

    if api == 'discover':
        print discover_tasks(server, port)
    elif api == 'stat':
        get_task_info(server, port, function, task_name)

