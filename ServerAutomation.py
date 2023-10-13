from operator import truediv
import shutil
import os
import time
import pathlib
import random
from os import path
import datetime

src_dir = os.listdir(os.getcwd() + '\\data')
print(src_dir)


def is_Hidden(file):
    return file.startswith('.')

def is_Organized(directory):
    wrk_dir = os.listdir(directory)
    for a in wrk_dir:
        if os.path.isdir(directory + '\\' + a):
            return False
    return True

#Navigates file system and removes non directories from the list
temp = []
for a in src_dir:
    if not os.path.isdir(os.getcwd() + '\\data\\' + a) or is_Hidden(a):
        temp.append(a)
for a in temp:
    src_dir.remove(a)
del temp


for a in src_dir:
    dir = os.getcwd() + '\\data\\' + a
    subDirs = os.listdir(dir)
    if not is_Organized(dir):
        for b in subDirs:
            subDir = dir + '\\' + b
            if os.path.isdir(subDir):
                files = os.listdir(dir)
                for c in files:
                    file = subDir + '\\' + c
                    shutil.copy2(file, dir)
                os.remove(subDir)
