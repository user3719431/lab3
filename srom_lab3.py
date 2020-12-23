import numpy as np
import math
from time import timeit

#m=431
#p(x) = x^431 + x^5 + x ^ 3 + 1
#поліноми мають вигляд sum_{i=o}^{430} a_{i}*x^{i}
#у векторному вигляді: [a0, a1, a2, a3, a4, ... , a430]
def addelem(f1, f2):
    g = []
    if len(f1) > len(f2):
        while len(f1) != len(f2):
            f2.insert(0, 0)
    elif len(f2) > len(f1):
        while len(f1) != len(f2):
            f1.insert(0,0)
    else:
        for in range(len(f1)): #xor між списками
            if (f1[i] = 0 and f2[j] = 0):
                g.append(0)
            elif (f1[i] = 0 and f2[j] = 1):
                g.append(1)
            elif (f1[i] = 1 and f2[j] = 0):
                g.append(1)
            else:
                g.append(0)
    return g
    
def mulelem(f1, f2):
    g = []
    i = 2m + 1
    k = 0
    while i != 0:
        g.append(0)
    while j in (len(f1)):
        while k in len(f2):
            if f1[i] = 1:
                if f2[j] = 0:
                    g[i+j] = 1
                else:
                    g[i+j] = 0
            else:
                if f2[j] = 0:
                    g[i+j] = 0
                else:
                    g[i+j] = 1
    t = 0
    while t < m:
        g.del[0]
    return g

def square(f1):
    g = []
    i = 0
    k = 0
    while k != 2m:
        g.insert(0,0)
        k = k + 1
    while i != m:
        g[2i] = f1[i]
        i = i + 1
    return g

def trace(f, m):
    g = 0
    k = 0
    i = len(f)
    while i != 0:
        while k != m:
            g[i ** (2 ** k)] = f[i ** (2 ** k)]
            k = k + 1
            i = i - 1
    return g
    
def step(f, d):
    g = []
    i = 0
    temp = 0
    while temp != 2m:
        g.append(0)
        temp = temp + 1
    while d != 0:
        while i != m:
        g[2i] = f1[i]
        i = i + 1
    return g