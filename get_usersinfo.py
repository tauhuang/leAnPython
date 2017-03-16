#!/usr/bin/python
# -*- coding: UTF-8 -*-
# get common user's informations which obtain username, home dir, shell from file '/etc/passwd'


with open('/etc/passwd') as ofile:
    with open('usersinfos.txt', 'w') as wfile:
        for line in ofile:
            linestr = line.split(':')
            if int(linestr[2]) > 999:
                wfile.write(linestr[0]+','+linestr[5]+','+linestr[6]+'\n')
