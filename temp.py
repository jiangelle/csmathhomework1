# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import random

x_max = 2*np.pi
n = 10

def sampleplot(k):
    return np.linspace(0,x_max,k)
    
x=sampleplot(100)
y=np.sin(x)
plt.plot(x,y,color="green")
plt.xlabel("x")
plt.ylabel("t")

a=sampleplot(n)
b=np.empty([n,1])
for i in range(n):
    b[i,:]=[np.sin(a[i])+random.gauss(0.1,0.1)]
plt.plot(a,b,'*')
'''
x1=np.empty([10,4])
for i in range(10):
    x1[i,:]=[a[i]**3,a[i]**2,a[i],1]
w = np.dot(np.linalg.pinv(x1),b)
p=np.poly1d(w.reshape(4))
plt.plot(x,p(x),color="blue")

'''
x2=np.empty([n,10])
for i in range(10):
    x2[i,:]=[a[i]**9,a[i]**8,a[i]**7,a[i]**6,a[i]**5,a[i]**4,a[i]**3,a[i]**2,a[i],1]
'''
w1=np.dot(np.linalg.pinv(x2),b)
p1=np.poly1d(w1.reshape(n))
plt.plot(x,p1(x),color="red")
print w1

'''
'''
def sampledot(k):
    a1=sampleplot(k)
    b1=np.empty([k,1])
    for i in range(k):
        b1[i,:]=[np.sin(a1[i])+random.gauss(0.1,0.1)]
    plt.plot(a1,b1,'.')
    x3=np.empty([k,10])
    for i in range(k):
        x3[i,:]=[a1[i]**9,a1[i]**8,a1[i]**7,a1[i]**6,a1[i]**5,a1[i]**4,a1[i]**3,a1[i]**2,a1[i],1]
    w2=np.dot(np.linalg.pinv(x3),b1)
    p2=np.poly1d(w2.reshape(10))
    plt.plot(x,p2(x),color="black")

sampledot(15)
sampledot(100)

'''
#+np.exp(-18)
temp1 = np.linalg.pinv(2*np.dot(np.transpose(x2),x2)+np.eye(10)*np.exp(-18))
temp2 =2*np.dot(np.transpose(x2),b)
w3 = np.dot(temp1,temp2)
p3=np.poly1d(w3.reshape(10))
plt.plot(x,p3(x),color="black")

