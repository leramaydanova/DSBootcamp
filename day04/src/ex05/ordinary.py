#! /usr/bin/python3

import sys, resource
from resource import *

def ordinary(path):
    file_list = []
    with open(path, 'r') as f:
        file_list = f.readlines()
    return file_list

if __name__ == '__main__':
    path = sys.argv[1]

    for item in ordinary(path):
        pass

    usage = resource.getrusage(RUSAGE_SELF)

    degree = 3
    if sys.platform == 'linux':
        degree = 2

    print(f"Peak Memory Usage = {usage.ru_maxrss / 1024**degree:.3f} GB\n\
User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:.2f}s")