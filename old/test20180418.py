a={'aa':'python','bb':'c++','cc':'JAVA'}
for name in sorted(a.values()):
	print(name.title()+",thank you for taking the poll.")

aliens = []
for alien in range(30):
	new_alien={'color':'green','print':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print("Total number od alien:"+str(len(aliens)))
