#!/usr/bin/env python3

import os
import configparser
import rich.progress

cp = configparser.ConfigParser()
cp.read_string("[_]\n" + open(os.path.expanduser("~/.mailhookrc"), "r").read())

CFG = dict(cp["_"])
print(CFG)


import subprocess

list_emlx = subprocess.check_output('find %s -name "*.emlx" -print0' % CFG['dir'], shell=True, universal_newlines=True).strip().split(chr(0))

for x in rich.progress.track(range(len(list_emlx)), "Loading all emlx files"):
    with open(list_emlx[x], 'r') as f:
        lines = f.read().strip().split("\n")
