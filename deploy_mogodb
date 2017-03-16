#!/usr/bin/python
# -*- coding: UTF-8 -*-
# deploy MongoDB using gzip-format file on Linux.


import subprocess
import os
# import fnmatch
import shutil


def write_log(logstr):
    with open('deployment.log', 'a') as log:
        log.write(logstr)


def exe_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        write_log('execute command ({0}) error. Message: {1}'.format(cmd, stderr))
        return p.returncode
    return p.returncode


def extract_gzipfile(filename):
    cmd = 'tar zvfx {0} -C ~/ --overwrite'.format(filename)
    returncode = exe_cmd(cmd)
    if returncode == 0:
        return True
    else:
        return False


def check_direxists(fullname):
    return os.path.exists(fullname)


def create_datadir(dirname):
    if check_direxists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    return dirname


def start_mongodb(datadir):
    fdir = os.path.expanduser('~')
    if check_direxists(datadir):
        pass
    else:
        return False
    # for i in fnmatch.filter(os.listdir(fdir), 'mongodb*'):
    #     if os.path.isdir(i) & check_direxists(i+'/bin'):
    #         write_log(i)
    #         returncode = exe_cmd("{0}/bin/mongod --dbpath {1}".format(i, datadir))
    #         if returncode == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    os.system(fdir+'/mongodb-linux-x86_64-rhel70-3.4.2/bin/mongod --dbpath '+datadir+' &')
    # returncode = exe_cmd(fdir+'/mongodb-linux-x86_64-rhel70-3.4.2/bin/mongod --dbpath '+datadir+' &')
    # if returncode == 0:
    #     return True
    # else:
    #     return False


def main():
    fdir = os.path.expanduser('~')
    extract_gzipfile(fdir+'/mongodb-linux-x86_64-rhel70-3.4.2.tgz')
    mongodata = create_datadir(fdir+'/mongodata')
    start_mongodb(mongodata)
    # returncode = start_mongodb(mongodata)
    # if returncode:
    #     print 'Start MongoDB successfully.'
    # else:
    #     print 'Start MongoDB unsuccessfully.Error in log file "deployment.log"'


if __name__ == '__main__':
    main()
