# -*- coding: utf-8 -*-
import subprocess

subprocess.check_output("/some_command", "args", shell=True, universal_newlines=True)
