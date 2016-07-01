convertee = raw_input('>>>').replace(' ', ' Space ')

hex_list = []

for i in convertee:
	hex_list.append(i.encode('hex'))

dec_list = []

for i in hex_list:
	try:
		int(i)
	except:
		alpha = int('0x'+str(i[1]), 16)

		print alpha

		print alpha*16**(len(str(i))-2)

		print i

		print int(i[0])*16**(len(str(i))-1)

		#RETURNS INCORRECT VALUE
		dec_list.append(int(i[0])*16**(len(str(i))-1) + alpha*16**(len(str(i))-2))

		print int(i[0])*16**(len(str(i))-1) + alpha*16**(len(str(i))-2)

		continue

	dec_list.append(int(i[0])*16**(len(str(i))-1) + int(i[1])*16**(len(str(i))-2))

print 'Hex List:', hex_list, '\nLength:', len(hex_list), '\nDec List', dec_list, '\nLength:', len(dec_list)
