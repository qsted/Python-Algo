# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def is_foo(par):
    if par=='foo':
        return True 
    else:
        return False
    
print(is_foo('yy'))


def factorial(n):
    if n<1:
        return 1
    else:
        return factorial(n-1)*n
    
print(factorial(10))

def find_larges(number):
    maxvalue=number[0]
    for value in number:
        if maxvalue< value:
            maxvalue=value
    return maxvalue

number=[100,99,200,110]
print(find_larges(number))

def average(table):
    if len(table)==0:
        return 0
    else:
        return sum(table)/len(table)
    
print(average(arr))


def is_bool(i,j):
    if i==1 or j==1 or i+j == 1:
        return True 
    else:
        return False 
    
print(is_bool(1,2))


def is_twin(a,b):
    a=a.lower()
    b=b.lower()
    if len(a) != len(b):
        return False
    else:
        a=sorted(a)
        b=sorted(b)
        return a==b
    
print(is_twin('abc','bca'))

def is_on_even_position(table, value):
    if value not in table:
        return False
    else:
        index = table.index(value)
        if index % 2==0:
            return True 
        return False
    
t=[0, 3, 1, 2, 4]
print(is_on_even_position(t,3))


def pi_approx(pts):
    count=0
    for x,y in pts:
        if x**2+y**2 <1:
            count+=1
    return 4*count/len(pts)

rands=[]
import random
for i in range(0,999):
    arr=[random.random(),random.random()]
    rands.append(arr)
    
print(pi_approx(rands))


def resharp(n,s):
    s=s.replace(' ','')
    newstr=''
    for i in range(len(s)):
        if i != 0 and i%n==0:
            newstr+='\n'+s[i]
        else:
            newstr+=s[i]
    return newstr

print(resharp(2,'1 23 456'))
        
def close_to_zero(ints):
    if ints:
        index=0
        for i in range(1,len(ints)):
            if abs(ints[index]) > abs(ints[i]):
                index=i
            elif abs(ints[index]) == abs(ints[i]) and ints[index]>ints[i]:
                index=i
        return ints[index]
    else:
        return 0

ints=[-9,8,2,1,-1,7]
print(close_to_zero(ints))
    





























