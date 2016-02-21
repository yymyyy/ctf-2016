import socket
import re
from ct import forge

s = socket.socket()
host = '188.166.133.53'
port = 10061
s.connect((host, port))

for i in xrange(20):
	received = s.recv(1024); print received
	received = s.recv(1024); print received

	ans = 'create 5000\n'
	s.send(ans)

	received = s.recv(1024); print received

	if 'Transaction' in received:
		ctx = received[len(received)-34:len(received)]
	print '[*] Verify ID: {0}'.format(ctx)

	received = s.recv(1024)

	ans = 'complete {0} {1}\n'.format(i, forge(ctx))
	print '[*] CMD: {0}'.format(ans)
	s.send(ans)

s.close()