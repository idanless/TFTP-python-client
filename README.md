# TFTP-python-clinet
Linux support only must install ATFTP\TFTP 
support Centos and ubuntu

use code example:

from TFTP_wrapper import TFTP
import glob

#upload all text file to demo directory 
for file in glob.glob("*.txt"):
    T = TFTP('X.X.X.X')
    print(file)
    T.PUT_witdirectory(file,'demo')

this basic use if needed 
