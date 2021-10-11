# TFTP-python-clinet
<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<p><strong>Linux support must install ATFTP\TFTP (yum or apt)</strong><br />support Centos and ubuntu</p>
<p>use code example:</p>
<p>from TFTP_wrapper import TFTP<br />import glob</p>
<p>#upload all text file to demo directory <br />for file in glob.glob("*.txt"):<br />T = TFTP('X.X.X.X')<br />print(file)<br />T.PUT_witdirectory(file,'demo')</p>
<p><span style="text-decoration: underline;">this basic use if needed</span> </p>
