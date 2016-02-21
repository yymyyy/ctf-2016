def forge(ctx):
	p = 'TRANSACTION: 5000'
	p += chr(0x09)*(17-len(p))
	p = p[::-1]
	ct = ctx
	ct = ct.decode('hex')
	ct = ct[::-1]
	update = []
	for ci,pl in zip(ct, p):
		x = ord(ci) ^ ord(pl)
		if pl == ':':
			break
		else:
			update.append(chr((ord('9') ^ x)).encode('hex'))
	update.reverse()
	return ctx[0:len(ctx)-10] + ''.join(update)

if __name__ == '__main__':
	ctx = '61426e0c6a0510423477791021596b4e75'
	print forge(ctx)