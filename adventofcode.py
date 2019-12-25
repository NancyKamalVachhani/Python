import math
def fuel(mass):
    #print("The fuel required is:")
    a=0
    n=mass/3
    a=math.floor(n)
    a=a-2
    #print(a)
    #else:
        #print("input should be greater than 6")
    return a
    
#m=int(input("Enter the mass ( in kilograms )"))
def calc(fname):
    f=open("fname.txt","r")
    s=0
    s=int(s)
    for line in f.readlines():
        p=fuel(int(line))
        s=s+p
    #print(sum)
    f.close()
    return s

t=calc("fname.txt")
print(t)

#60