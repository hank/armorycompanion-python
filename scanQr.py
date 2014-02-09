#!/usr/bin/env python
import os, subprocess, re

if __name__ == "__main__":
	p = subprocess.Popen(["zbarcam", "--prescale=640x480"], 
		stdout=subprocess.PIPE)
	output = ''
	while True:
		line = p.stdout.readline()
		output += line
		if line != '':
			if re.search(r'END-TRANSACTION', line):
				break
	p.terminate()
	p.wait()
	with open(os.path.join(os.environ['HOME'], 'Desktop', 'scanned.unsigned.tx'), 'w') as f:
 		f.write(output)
