age=10
message="happy " + str(age) + "rd Birthday!"

print(message)

a=['123','32','32','333']
print(a)
del a[0]
print(a)
a.insert(1,'999')
print (a)


a[0]=908

print(a)

b=a.pop()
print (a)

print (b)

a.remove('999')

print (a)


p=['ken','java','linux','c++']
p[0]='doc'
ppp=p.pop()
del p[0]

p.insert(0,'python')
print(p)
p.reverse()
print(p)

print(sorted(p))
print(p)

print(p[-3])
