#execute shell commands from python

import subprocess

proc = subprocess.run(["ls","-l"])