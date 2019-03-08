def get_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

a=get_name('jack','well')
print(a)



def person(a_name,b_name):
    nper={'first':a_name,'last':b_name}
    return nper

q=person('jimi','hendrix')
print (q)


while True:
    print ("\nPlease tell me your name:")
    print ("(Enter 'q' at any time to quit)")

    f_name=input("First name:")
    if f_name=='q':
        break

    l_name=input("Last name:")
    if l_name=='q':
        break

    name=get_name(f_name,l_name)
    print ("\nHello, "+name+"!")