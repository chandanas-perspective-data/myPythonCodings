import re
import random

names = ["Anil", "kamesh", "rajesh", "ramya", "sunil", "suresh", "anil", "venkat"]

def listings():
    list= []
    x = 100000
    for i in range(x):
        l = random.choice(names)
        list.append(l)

def diction():
    d= {}
    x =100000
    count =0
    for j in range(x):
        l = random.choice(names)
        d[count] = l
        count +=1
    #print (d)

import time

t1 = time.time()
listings()
t2 = time.time()

print (t2-t1)


t3 = time.time()
diction()
t4 = time.time()

print (t4-t3)