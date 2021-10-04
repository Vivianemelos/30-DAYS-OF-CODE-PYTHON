#!/bin/python3

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