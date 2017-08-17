#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os


def have_permission(file_or_dir_name, perm_mode):
    """have_permission(file_or_dir_name, perm_mode)    return bool True if having "perm_mode" permission 
    file_or_dir_name is string.
    perm_mode is string.It can be "r", "w", "x" or consist of the three letters.
    r: read permission
    w: write permission
    x: executed permission
    You can combine any of "r", "w", "x".e.g. "rw" for read and write permission.
    """
    return_bool = True
    perm_dict = {"r": os.R_OK, "w": os.W_OK, "x": os.X_OK}
    for i in perm_mode:
        return_bool = (os.access(file_or_dir_name, perm_dict[i]) and return_bool)
    return return_bool


if __name__ == "__main__":
    have_permission("abc.txt", "rwx")
    
