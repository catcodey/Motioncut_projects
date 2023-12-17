import random
import string
spl_list=['!','@','#','$','%','^,&','<','*','(',')']
print("\t\t\tPassword Generator\n")
l=[]
nofpw=int(input("enter number of passwords: "))
for i in range(nofpw):
    length=int(input("enter length of password: "))
    while length<4:
        print("minimum password length is 4")
        length=int(input("enter length of password: "))
  
    for i in range((length//4)+1):
        
        upper= random.choice(string.ascii_uppercase)
        lower= random.choice(string.ascii_lowercase)
        number= random.randint(0, 10)
        spl= random.choice(spl_list)
        l.append(upper)
        l.append(lower)
        l.append(str(number))
        l.append(spl)
        
    random.shuffle(l)
    print("Password: ","".join(l))
    l=[]
        
