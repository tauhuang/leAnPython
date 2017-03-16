#!/usr/bin/python
# -*- coding: UTF-8 -*-
# get common user's informations which obtain username, home dir, shell from file '/etc/passwd'

def main():
    backup_file = 'userinfo.txt'
    with open('/etc/passwd') as source, open(backup_file, 'w') as target:
        for line in source:
            data = line.split(':')
            user, home, shell = data[0], data[5], data[6].strip
            target.write("{0},{1},{2}\n".format(user, home, shell))
            
            
if __name__ == '__main__':
    main()
