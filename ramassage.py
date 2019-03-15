#!/usr/bin/env/python3

import os
import subprocess
import sys


def helper():
    print("USAGE:")
    print("\tpython ramassage.py <repo_name> <list_of_students>")


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False


def clone(student_dir):

    command = "git clone git@git.epitech.eu:/" + student_dir + "/" + sys.argv[1]
    print("\nFrom repository " + student_dir + "\n")
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).wait()
    if os.path.exists(sys.argv[1]):
        os.rename(sys.argv[1], "directories/" + student_dir)


def core():
    if len(sys.argv) == 3:
        fl = open(sys.argv[2])
        i = 0
        ensure_dir("directories")
        for elem in fl.readlines():
            if ensure_dir("directories/" + elem.replace("\n", "")):
                clone(elem.replace("\n", ""))
        fl.close()
    else:
        helper()
        exit()


if __name__ == '__main__':
    core()