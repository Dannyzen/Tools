import os.path as path
import time
import os
from datetime import datetime



def main():
    recentChecker('file.txt','deploy.lock',600)
def getFileTime(file):
    file_time = path.getmtime(file)
    return file_time
def getCurrentTime():
    now = time.time()
    return now
def calcHowLong(current_time, file_time):
    how_long = current_time - file_time
    return how_long
def lockMaker(filename):
    open(filename,'w')
def recentChecker(filename, lockfile, maxtime):
    """
    #debug
    print getCurrentTime()
    print getFileTime(filename)
    print calcHowLong(getCurrentTime(), getFileTime(filename))
    """
    if calcHowLong(getCurrentTime(), path.getmtime(filename)) > maxtime:
        lockMaker(lockfile)
    else:
        try:
            os.remove(lockfile)
        except OSError:
            pass

if __name__ == "__main__":
        main()
