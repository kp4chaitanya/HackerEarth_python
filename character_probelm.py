#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:00:05 2023

@author: chay
"""

def StringCheck(a):
    b=set(a)
    c=list(b)
    first=c[0]
    second=c[1]
    print("First element is :", first)
    print("Second element is :", second)
    
    d=list(a)
    #counter for Z
    x=a.count(first)
    #counter for O
    y=a.count(second)
    
    print("Z count is ", x)
    print(" O count is ", y)
    
    if(2*x==y):
        print("Yes")
    
    else:
        print("No")


A=input()
StringCheck(A)
    
        #zzzzzzoooooooooooo