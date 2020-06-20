
# coding: utf-8

# In[10]:


class PerHealth:
    Normal,Infected,Recovered,Dead=range(4)


# In[11]:


import random
import math

class Person(object):
    h=""
    def __init__(self,health):
        self.x=random.uniform(0,5)
        self.y=random.uniform(0,5)
        self.health=health
        self.neighbour=[]
        self.badneighbour=0
    
    def __str__(self):
        if (self.health==PerHealth.Normal):
            h='Normal'
        elif (self.health==PerHealth.Infected):
            h='Infected'
        elif (self.health==PerHealth.Dead):
            h='Dead'
        else:
            h='Recovered'
        return("This person with id {}  at location {:.2f}, {:.2f} is ".format(id(self),self.x,self.y)+h)
            
    def Distance(self,z):
        result=math.sqrt((z.x-self.x)**2 + (z.y-self.y)**2)
        return(result)
        
    def NearMe(self,j):
        d=self.Distance(j)
        if(d<0.2):
            self.neighbour.append(j)
      
    def Neighbours(self):
       # print(self,"->",len(self.neighbour),"Neighbours")
        self.badneighbour=len(self.neighbour)
        #for n in self.neighbour:
         #   print(n)
        
    def Locate(self):
        return(self.x,self.y)
   
    def InfectNeighbour(self):
        if (self.health==PerHealth.Infected):
            for i in self.neighbour:
                if(i.health==PerHealth.Normal):
                    i.health=PerHealth.Infected    


# In[12]:


x=[]
y=[]
x1=[]
y1=[]
p=[]
for i in range(450):
    per=Person(PerHealth.Normal)
    x.append(per.Locate()[0])
    y.append(per.Locate()[1])
    p.append(per)
for i in range(50):
    per=Person(PerHealth.Infected)
    x1.append(per.Locate()[0])
    y1.append(per.Locate()[1])
    p.append(per)


# In[13]:


def Listppl(p):
    xn=[]
    xi=[]
    yn=[]
    yi=[]
    for i in p:
        if(i.health==PerHealth.Normal):
            xn.append(i.Locate()[0])
            yn.append(i.Locate()[1])
        elif(i.health==PerHealth.Infected):
            xi.append(i.Locate()[0])
            yi.append(i.Locate()[1])
    return(xn,yn,xi,yi)      


# In[14]:


p1=[]
for i in range(500):
    for j in range(500):
        p1.append(p[i].Distance(p[j]))
        p[i].NearMe(p[j])
for i in range(500):
    p[i].Neighbours()
hist=[]
for i in p:
    hist.append(i.badneighbour)
            
        
        


# In[15]:


import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.scatter(x1,y1,color='red')


# In[16]:


import matplotlib.pyplot as plt
for i in p:
    i.Neighbours()
    i.InfectNeighbour()
xn,yn,xi,yi=Listppl(p)    
plt.scatter(xn,yn)
plt.scatter(xi,yi,color='red')   


# In[17]:


import matplotlib.pyplot as plt
plt.hist(hist, bins=20,range=(0,10))


# In[18]:


class Simulator(object):
    def __init__(self):
        self.time=0
        self.People=500
        self.plist=[]
        


# In[ ]:



 

