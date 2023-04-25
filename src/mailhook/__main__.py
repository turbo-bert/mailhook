#!/usr/bin/env python3

import os
import configparser

cp = configparser.ConfigParser()
cp.read_string("[_]" . open(os.path.expanduser("~/.mailhookrc"), "r").read())

CFG = dict(cp["_"])
print(CFG)
