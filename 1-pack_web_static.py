#!/usr/bin/python3
'''
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
'''

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''function'''
    local("mkdir -p versions/")
    now = datetime.now()
    file_time = now.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(file_time)
    try:
        local("tar -cvzf " + file_name + " web_static")
        return "{}".format(file_name)
    except as Exception:
        return None
