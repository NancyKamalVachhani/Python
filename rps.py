import random
l=['r','s','p']      
print("enter your choice")
print("r=rock")
print("s=scissor")
print("p=paper")
u=input("Enter your choice")

l1=['r','s','p']
n=random.choice(l1)
print(n)

if u=='r':
    if n=='r':
        print("Draw")
    
    elif n=='p':
        print("Machine wins")
        
    elif n=='s':
        print("User wins")
        
elif u=='p':  
    if n=='r':
        print("User wins")
    
    elif n=='p':
        print("Draw")
        
    elif n=='s':
        print("Machine wins")
        
elif u=='s':
    if n=='r':
        print("Machine wins")
    
    elif n=='p':
        print("User wins")
        
    elif n=='s':
        print("Draw")



#output
enter your choice
r=rock
s=scissor
p=paper
Enter your choicer
r
Draw