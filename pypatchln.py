#!/usr/bin/env python

import os
import string


keyString = "libboost_"
notSring = "1.53.0"

for i in os.listdir():
	if keyString in i:
		if notSring not in i:
			oldName = i
			newName = i + ".1.52.0"
			os.symlink(oldName, newName, target_is_directory=False, dir_fd=None)
			print(i);






