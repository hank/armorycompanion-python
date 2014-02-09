Armory Companion Python
=======================

The Armory Companion Android app can scan any Base64-encoded signed bitcoin
transaction from any bitcoin client, but the main client it's been built for,
of course, is Armory.  On the offline machine, to ease scanning and conversion
to QR codes, you'll need some python scripts.  These are really simple scripts,
and as such are auditable by even casual users.  Make sure to look through
the code before using it - it will help you sleep better at night knowing
there's nothing malicious there.

The following packages were required to get Ubuntu 12.04 x64 working with
these scripts:

* python-pkg-resources
* python-support
* python-imaging
* libpng12-0
* libzbar0
* liblqr
* zlib1g
* libmagickcore4
* imagemagick-common
* libgomp
* libjpeg8
* libmagickwand4
* libv4l
* libv4lconvert
* zbar-tools

I also needed the following Python libraries (install with setup.py)

* [python-qrcode](https://github.com/lincolnloop/python-qrcode) 
* [six](https://pypi.python.org/pypi/six)

Feel free to let me know using the issue tracker here if there are more
packages required when you try it, or if you have a list of packages and/or
steps to do this on another platform or GNU/Linux distribution.  I'll try
to integrate any guidance into the documentation here.

## Requirements
* A working knowledge of bitcoin
* A working knowledge of how offline wallets work (see [here](https://bitcoinarmory.com/about/using-our-wallet/) for Armory's description)
* Ability to install and use Linux and run python scripts
* Laptop for use as a cold wallet with a webcam that works in Linux with zbar
* USB Key for initial transfer of code/packages to offline laptop
* Android device that will run the Armory Companion Android app

## Howto
There's a step-by-step video [here](http://www.youtube.com/watch?v=ZlSC3mLjNSg).
The basic steps are as follows:
* Set up you offline laptop, preferably with Ubuntu 12.04
* Install Armory 0.90-beta or better on it offline
* Create some offline wallets and move the watch-only wallets to your online Armory instance.
* Install packages above with dpkg from a USB drive or the like
* Copy scripts in this repository to the offline machine
* Try running them, report any problems in the issue tracker
* Once everything looks like it's going to work, go to the online Armory instance and make a
  new offline transaction.  
* Create a QR code of the transaction (I used QREncoder from the App Store on my Mac)
* Take a picture with your phone and display it as large as you can on the screen
* Run scanQR.py.  This will open the video webcam scanning window.  Hold the
  phone up and scan the transaction.
* Once the scan works, the video window will close and a new file should appear
  on the desktop.  It will be named scanned.unsigned.tx.
* Use the Offline Transactions feature of Armory to read the file in and sign it.  This process
  will delete the unsigned transaction file and replaced it with a signed
  transaction file (scanned.signed.tx)
* Run the qrSignedTx script with the signed file as a parameter.  It will dump out a QR code.
  If you use the included desktop shortcut file, you can just drag and drop it on the icon, and
  it will automatically make an appropriately-sized terminal for scanning.
* Scan the new QR code with the Armory Companion Android app and broadcast it.

Note that access to the online computer is only needed for creating the initial transaction.
All further actions are performed either on the offline computer or the Android device.

## Moving parts

### scanQr.py
This script shows a video webcam window and attempts to scan a QR code.  If you show it
an Armory unsigned transaction, it will write it to a file on the desktop and exit.

### qrSignedTx.py
This script, when run with a single parameter (the file containing the signed transaction)
will use Armory's python library to convert it to a bitcoin message, Base64 encode it, and
produce a QR code in the terminal containing it.  This can be scanned and used with any
bitcoin client (the Android Armory Companion app uses bitcoinj).

### Desktop shortcuts
These are optional, and are just handy to have on the desktop in order to use the scripts.
You'll have to adjust them to match your paths on your offline machine if you want to use them.
