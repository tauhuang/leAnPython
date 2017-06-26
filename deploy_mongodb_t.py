#!/usr/bin/python
# -*- coding: UTF-8 -*-
# deploy MongoDB using gzip-format file on Linux.


import os
import shutil
import tarfile


def prepare_env(data_dir, package):
    package_dir = os.path.splitext(package)[0]
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.mkdir(data_dir)
    # tar mongo package
    t = tarfile.open(package, 'r')
    t.extractall('.')


def main():
    data_dir = os.path.join(os.path.expanduser('~'), 'mongodata')
    package = 'mongodb-linux-x86_64-rhel70-3.4.2.tgz'
    if not os.path.exists(package):
        raise SystemExit("{0} not found".format(package))
    prepare_env(data_dir, package)
    package_dir = os.path.splitext(package)[0]
    mongod = os.path.join(os.path.realpath('.'), package_dir, 'bin', 'mongod')
    os.system("{0} --dbpath {1} &".format(mongod, data_dir))


if __name__ == '__main__':
    main()
