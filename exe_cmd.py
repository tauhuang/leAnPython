#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import logging as LOG
def execute_cmd(cmd):
    LOG.debug('ready to execute command : {0} '.format(cmd))
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        LOG.debug("execute command ({0}) error ({1})".format(cmd, stderr))
        return p.returncode, stderr
    return p.returncode, stdout


cmd = raw_input("input shell commmand:")
returncode, stdout = execute_cmd(cmd)
print returncode
print stdout
