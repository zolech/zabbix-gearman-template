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

if __name__ == '__main__':
    server = sys.argv[1]
    port = sys.argv[2]
    api = sys.argv[3]

    if api == 'discover':
        print discover_tasks(server, port)
