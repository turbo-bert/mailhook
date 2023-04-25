#!/usr/bin/env python3

import os
import sys
import configparser
import rich.progress

cp = configparser.ConfigParser()
cp.read_string("[_]\n" + open(os.path.expanduser("~/.mailhookrc"), "r").read())

CFG = dict(cp["_"])
print(CFG)


import subprocess

list_emlx = subprocess.check_output('find %s -name "*.emlx" -print0' % CFG['dir'], shell=True, universal_newlines=True).strip().split(chr(0))[0:-1]

for x in rich.progress.track(range(len(list_emlx)), "Loading all emlx files"):
    with open(list_emlx[x], 'r') as f:
        try:
            lines = f.read().strip().split("\n")
            lines = lines[1:]
            killstart = len(lines)-1
            while killstart > 0 and not lines[killstart].startswith("<?xml version"):
                killstart-=1
            lines = lines[0:killstart]
            print(lines)
            sys.exit(0)
        except:
            pass