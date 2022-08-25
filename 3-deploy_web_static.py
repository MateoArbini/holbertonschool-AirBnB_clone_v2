#!/usr/bin/python3
'''
script that creates and distributes an archive to your web server, using
the funtion deploy()
'''

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.175.220.232', '54.221.168.160']


def do_pack():
    '''function'''
    local("mkdir -p versions/")
    now = datetime.now()
    file_time = now.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(file_time)
    try:
        local("tar -cvzf " + file_name + " web_static")
        return "{}".format(file_name)
    except Exceptions:
        return None


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
        except Exceptions:
            return False


def deploy():
    '''function'''
    path = do_pack()
    if os.path.exists(path):
        return do_deploy(path)
    else:
        return False
