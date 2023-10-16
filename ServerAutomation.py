from operator import truediv
import shutil
import os
import time
import pathlib
import random
from os import path

import datetime
import sched


src_dir = os.listdir(os.getcwd() + '\\data')

#checks if a file is hidden or not
def is_Hidden(file):
    return file.startswith('.')

#checks if a directory is already condenced
def is_Organized(directory):
    wrk_dir = os.listdir(directory)
    for a in wrk_dir:
        if os.path.isdir(directory + '\\' + a):
            return False
    return True

def ServerAutomation(scheduler):
    #Copies up Files that are in there directories and deletes them
    for a in src_dir:
        dir = os.getcwd() + '\\data\\' + a
        subDirs = os.listdir(dir)
        if not is_Organized(dir):
            for b in subDirs:
                subDir = dir + '\\' + b
                if os.path.isdir(subDir):
                    files = os.listdir(subDir)
                    for c in files:
                        file = subDir + '\\' + c
                        shutil.copy(file, dir)
                        os.remove(file)
                    os.rmdir(subDir)


    #Renames and dates everything
    for a in src_dir:
        dir = os.getcwd() + '\\data\\' + a
        files = os.listdir(dir)
        count = 0
        for b in files:
            count += 1
            #we rename the files to temp names to prevent 
            os.rename('data\\' + a + '\\' + b, 'data\\' + a + '\\' + 'temp' + b)
        count += 1
        usedNums = [0]
        for b in files:
            file = dir + '\\' + b
            loop = True
            attempt = 0
            while(loop):
                attempt = random.randrange(count)
                loop = False
                for d in usedNums:
                    if attempt == d:
                        loop = True
            usedNums.append(attempt)
            print('Original Name and Date')
            print(b)
            print(os.path.getctime('data\\' + a + '\\' + 'temp' + b))
            print('\n')
            creation_date = time.time() - random.randrange(864000)
            os.utime('data\\' + a + '\\' + 'temp' + b, (creation_date, creation_date))
            os.rename('data\\' + a + '\\' + 'temp' + b, 'data\\' + a + '\\' + str(attempt) + b[-4:])
            print('New Name and Date')
            print(str(attempt) + b[-4:])
            print(creation_date)
            print('\n')
    my_scheduler.enter(30, 1, ServerAutomation, (scheduler,))



#Navigates file system and removes non directories from the list
temp = []
for a in src_dir:
    if not os.path.isdir(os.getcwd() + '\\data\\' + a) or is_Hidden(a):
        temp.append(a)
for a in temp:
    src_dir.remove(a)
del temp

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(0, 1, ServerAutomation, (my_scheduler,))
my_scheduler.run()


