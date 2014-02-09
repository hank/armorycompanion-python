#!/usr/bin/env python
import sys, os, subprocess, base64
import qrcode
sys.path.append(os.path.join('/usr', 'lib', 'armory'))
from armoryengine import *
def usage():
	print "Usage: %s SIGNED-TX-FILE" % (__file__,)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
		sys.exit(2)
	# Read signed tx from file
	f = open(sys.argv[1], 'r')
	fileContent = f.read()
	# Create armory object representing tx
	proposal = PyTxDistProposal()
	proposal.unserializeAscii(fileContent)
	proposal.pprint()
	print "Preparing final TX"
	finalTx = proposal.prepareFinalTx()
	print "Generating QR Code"
	serialized = finalTx.serialize()
	armored = base64.b64encode(serialized)
	qr = qrcode.QRCode()
	qr.add_data(armored)
	qr.print_tty()
	raw_input("Press ENTER to exit")
	
