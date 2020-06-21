#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

def run(task):
    print(task)
    subprocess.call(["rsync", "-varq", task, dest])

src = "data/prod/"
dest = "data/prod_backup/"

dir_tasks = [os.path.join(src, x) for x in os.listdir(src)]
p = Pool(len(dir_tasks))
p.map(run, dir_tasks)

