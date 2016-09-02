#!/usr/bin/python
import gearman
import json
import sys

gm_admin_client = gearman.GearmanAdminClient(['172.25.10.81:4730'])


def discover_tasks():
    d = {'data': []}
    for task in gm_admin_client.get_status():
        d['data'].append({'{#TASK}': task['task']})
    return json.dumps(d, indent=1)

if __name__ == '__main__':
    print discover_tasks()
