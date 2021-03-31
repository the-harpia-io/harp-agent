import os
import harp_agent.settings as settings
import json
import errno
import pwd
import grp


def create_config_file():
    with open(settings.PATH_TO_MS_CONFIG, 'w+') as outfile:
        json.dump({}, outfile)


def create_folders():
    directories = ['/etc/harp-gate-client', '/var/log/harp-gate-client']
    uid = pwd.getpwnam("root").pw_uid
    gid = grp.getgrnam("root").gr_gid
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.chown(directory, uid, gid)
