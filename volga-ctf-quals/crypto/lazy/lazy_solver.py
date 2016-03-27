from collections import defaultdict
import hashlib
import itertools
import string
import socket
import struct
from server import *

keys_file_path = '.'

def sha1(s):
	m = hashlib.sha1()
	m.update(s)
	return m.digest()

def powork(prefix):
	letters = string.ascii_letters + string.digits + string.ascii_letters + string.digits
	for c in itertools.combinations_with_replacement(letters, 5):
		s = ''.join(c)
		full = prefix + s
		if sha1(full).endswith('\xff\xff\xff'):
			return full


h1 = SHA1('exit')
h2 = SHA1('leave')
r = 618115531371374705088478644225735834217345085623
s1 = 172143370381913466209965676314309162396852880243
s2 = 132450039864758067994560555212301135386357959258

p, q, g, y = import_public_key(keys_file_path)

k = (invert((s1-s2),q)*(h1-h2)) % q
x = -(invert(r*(s2-s1),q)*(s2*h1-s1*h2)) % q

f = open('key.private','w')
for item in (p, q, g, x, y):
	f.write(str(item))
	f.write('\n')
f.close()

cmd = 'cat flag.txt'
f = open('{0}.sig'.format(cmd),'w')
for item in sign(cmd, p, q, g, x, k):
    f.write(str(int(item)))
    f.write('\n')
f.close()

s = socket.socket()
host = 'lazy.2016.volgactf.ru'
port = 8889
s.connect((host, port))

r = s.recv(1024)
prefix = r[-16:]
send_message(s, powork(prefix))

f = open('{0}.sig'.format(cmd)).read().rstrip() +'\n'+ cmd 
send_message(s, f)

flag = s.recv(1024)
print flag

s.close()
