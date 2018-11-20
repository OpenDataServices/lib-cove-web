import datetime
import fcntl
import json
import os
import requests


def get_orgids_prefixes(orgids_url=None):
    '''Get org-ids.json file from file system (or fetch upstream if it doesn't exist)

    A lock file is needed to avoid different processes trying to access the file
    trampling each other. If a process has the exclusive lock, a different process
    will wait until it is released.
    '''
    local_org_ids_dir = os.path.dirname(os.path.realpath(__file__))
    local_org_ids_file = os.path.join(local_org_ids_dir, 'org-ids.json')
    lock_file = os.path.join(local_org_ids_dir, 'org-ids.json.lock')
    today = datetime.date.today()
    get_remote_file = False
    first_request = False

    if not orgids_url:
        orgids_url = 'http://org-id.guide/download.json'

    if os.path.exists(local_org_ids_file):
        with open(lock_file, 'w') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            fp = open(local_org_ids_file)
            org_ids = json.load(fp)
            fp.close()
            fcntl.flock(lock, fcntl.LOCK_UN)
        date_str = org_ids.get('downloaded', '2000-1-1')
        date_downloaded = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        if date_downloaded != today:
            get_remote_file = True
    else:
        get_remote_file = True
        first_request = True

    if get_remote_file:
        try:
            org_ids = requests.get(orgids_url).json()
            org_ids['downloaded'] = "%s" % today
            with open(lock_file, 'w') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                fp = open(local_org_ids_file, 'w')
                json.dump(org_ids, fp, indent=2)
                fp.close()
                fcntl.flock(lock, fcntl.LOCK_UN)
        except requests.exceptions.RequestException:
            if first_request:
                raise  # First time ever request fails
            pass  # Update fails

    return [org_list['code'] for org_list in org_ids['lists']]
