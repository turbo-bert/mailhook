#!/usr/bin/env python3

import os
import configparser

cp = configparser.ConfigParser()
cp.read_string("[_]\n" + open(os.path.expanduser("~/.mailhookrc"), "r").read())

CFG = dict(cp["_"])
print(CFG)


import subprocess

list_emlx = subprocess.check_output('find %s -name "*.emlx" -print0' % CFG['dir'], shell=True, universal_newlines=True).split(chr(0))

print(list_emlx)
