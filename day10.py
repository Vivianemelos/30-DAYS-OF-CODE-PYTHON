#!/bin/python3
# Solução O(n²)
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    cont = 0
    l = []
    while n > 0:
        while n%2!=0:
            cont = cont + 1
            n = n//2
        l.append(cont)   
        cont = 0 
        n = n//2
print(max(l))

#Solução O(n)
  count, max = 0, 0;
    while (n > 0):
        if n % 2 == 1:
            count+=1
            if count > max:
                max = count
            
        else:
            count = 0
        
        n = n / 2;
   
