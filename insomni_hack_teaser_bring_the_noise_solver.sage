import os
import hashlib
import itertools
import string
import socket
from subprocess import check_output

def md5(s):
	m = hashlib.md5()
	m.update(s)
	return m.hexdigest()

def powork(challenge):
	letters = string.printable
	for c in itertools.combinations_with_replacement(letters, 4):
		s = ''.join(c)
		if md5(s).startswith(challenge):
			return s.encode('hex')

# socket
sock = socket.socket()
sock.connect(('bringthenoise.insomnihack.ch',1111))
print '[*] Connect ...'

# grab challenge
r = sock.recv(4096)
if 'Challenge = ' in r:
	challenge = r.replace('Challenge = ','').rstrip()

print '[*] Challenge: {0}'.format(challenge)

# proof of work
powork_r = powork(challenge)
print '[*] Proof of work: {0}'.format(powork_r)

# send powork
sock.send(powork_r.decode('hex')+'\n')

# see response
r = sock.recv(4096)
if ',' in r:
	data = [int(x) for x in r if x.isdigit()]
	result = data[len(data)-1]
	del data[len(data)-1]
	coefs = data

print '[*] Coefs: {0}'.format(coefs)
print '[*] Result: {0}'.format(result)

# see equation
r = sock.recv(4096)
print r

equation = r.split('\n')
del equation[len(equation)-1]
del equation[len(equation)-1]

print '[*] Equation: {0}'.format(equation)

# find solution
print '[*] Find solution ...'
from collections import defaultdict
import itertools
import struct
import os

def get_common_element(L):
	d = defaultdict(int)
	for i in L:
	    d[i] += 1
	result = max(d.iteritems(), key=lambda x: x[1])
	return result

def chunks(l, n):
	n = max(1, n)
	return [l[i:i + n] for i in range(0, len(l), n)]

sol_st = []
a,b,c,d,e,f = var('a,b,c,d,e,f')

sol = 'abcdef'

equs = equation
equu = chunks(equs, 6)

for i in xrange(2):
	equ = equu[i]
	cdd_dt = []
	cnt = 0
	for r in xrange(len(equ)):
		if cnt == 6:
			break
		else:
			dt = [int(x) for x in equ[r] if x.isdigit()]
			res = dt[len(dt)-1]
			del dt[len(dt)-1]
			coefs = dt
			poly = ''
			for i in xrange(len(coefs)):
				poly += '{0}*{1} + '.format(str(coefs[i]), sol[i])
			cdd = '{0} + v + 8 == {2}'.format(poly[0:len(poly)-3], i,str(res))
			cdd_dt.append(cdd)
			cnt += 1

	bforce = open('/ctf/insomnihack2016/crypto/bring_the_noise/66abc.txt')
	for l in bforce:
		l = list(l.rstrip())
		nl = ['-1' if x == '2' else x for x in l ]
		listing = ''
		for i in xrange(len(cdd_dt)):
			listing += '{0}, '.format(cdd_dt[i].replace('v', nl[i]))
		exec('eqn = [{0}]'.format(listing[0:len(listing)-2]))
		solution = solve_mod(eqn, 8)
		if len(solution) > 0:
			for x in solution:
				sol_st.append(x)

sol, y = get_common_element(sol_st)

sol = ', '.join([ str(x) for x in sol ])

# send solution
solution = sol
print '[*] Solution: {0}'.format(solution)
sock.send(solution+'\n')

# see response wroing
r = sock.recv(4096)
if 'Wrong' in r:
	print r
elif 'INS' in r:
	print r

r = sock.recv(4096)
print '[*] FLAG: {0}'.format(r)

sock.close()
