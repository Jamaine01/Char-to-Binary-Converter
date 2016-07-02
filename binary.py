convertee = raw_input('>>>')

hex_list = []

for i in convertee:
	hex_list.append(i.encode('hex'))

dec_list = []

for i in hex_list:
	try:
		int(i)
	except:
		alpha = int('0x'+str(i[1]), 16)

		dec_list.append(int(i[0])*16**(len(str(i))-1) + alpha*16**(len(str(i))-2))

		continue

	dec_list.append(int(i[0])*16**(len(str(i))-1) + int(i[1])*16**(len(str(i))-2))

print 'Hex List:', hex_list, '\nLength:', len(hex_list), '\nDec List', dec_list, '\nLength:', len(dec_list)

binary_base = [1,2,4,8,16,32,64,128]

binary_done = []

for i in dec_list:
	for b in binary_base:
		while True:
			if i < b:
				maxim = binary_base.index(b) + 1
				rev_base = binary_base[0:maxim]

				rev_base = list(reversed(rev_base))
				
				count = 0
				for n in rev_base:
					if i >= n:
						binary_done.append('1')
						i = i - n
						count = count + 1
						if count == b:
								break
					else:
						binary_done.append('0')
						count = count + 1
						if count == b:
								break
			break

print str(binary_done).replace('[', '').replace(']', '').replace("'", '').replace(',', '')