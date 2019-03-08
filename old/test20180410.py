a=(200,50)
print(a[0])

print(a[1])

for b in a:
	print(b)


k=['abc','def','ghi','jkl','mno']
for kk in k:
	if kk!='abc':
		print(kk.upper())
	else:
		print('false')		


dd=10
print(dd<20)
print(dd>20)
print(dd==20)
print(dd!=20 or dd>20)


black=['ken','annt','pan','honly']
username='pa'
if username not in black:
	print(username.title()+",you can enter!")
else:
	print(username.title()+",sorry !")
