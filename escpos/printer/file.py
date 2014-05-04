#!/usr/bin/python
'''
@author: Manuel F Martinez <manpaz@bashlinux.com>
@organization: Bashlinux
@copyright: Copyright (c) 2012 Bashlinux
@license: GPL
@contributor: Lewis Eason <me@lewiseason.co.uk>
'''

from escpos import *

class File(escpos.Escpos):
    """ Define Generic file printer """

    def __init__(self, devfile="/dev/usb/lp0"):
        """
        @param devfile : Device file under dev filesystem
        """
        self.devfile = devfile
        self.open()


    def open(self):
        """ Open system file """
        self.device = open(self.devfile, "wb")

        if self.device is None:
            print "Could not open the specified file %s" % self.devfile


    def _raw(self, msg):
        """ Print any command sent in raw format """
        self.device.write(msg);


    def __del__(self):
        """ Close system file """
        self.device.close()

Printer = File