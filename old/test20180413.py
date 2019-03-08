
a={'color':'blue','print':10}
print(a['color'])
print(a['print'])
print('You just earned '+str(a['print'])+' prints')


a['postion']=0
a['postion1']=10

print(a)


alien={'x':0,'y':5,'speed':'slow'}
if alien['speed']=='medium':
	new_x=2
elif alien['speed']=='slow':
	new_x=5
else:
	new_x=10
alien['x']=alien['x']+new_x
print('New x: '+str(alien['x']))