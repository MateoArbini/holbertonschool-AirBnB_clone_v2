#!/usr/bin/python3
'''
script that distributes an archive to your web servers, using the function
do_deploy
'''

from fabric.api import *
import os


env.hosts = ['35.175.220.232', '54.221.168.160']


def do_deploy(archive_path):
    '''function'''
    if not os.path.exists(archive_path):
        return False
    else:
        try:
            put(archive_path, '/tmp/')
            path_name = archive_path.split('/')
            path_name_d = path_name[1].split('.')
            file_name = "/data/web_static/releases/" + path_name_d[0] + "/"
            run("mkdir -p" + " " + file_name)
            run("tar -xzf /tmp/" + path_name[1] + " -C" + file_name)
            run("rm /tmp/" + path_name[1])
            run("mv " + file_name + "web_static/*" + " " + "/" + file_name)
            run("rm -rf " + file_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + file_name + " " + "/data/web_static/current")
            print("New version deployed!")
            return True
        except:
            return False
