#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
def Arredonda(n):
    return int(n + (0 if n % 1 ==  0 else 1)) 

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = tip_percent * meal_cost / 100
    tax_percent = tax_percent * tip_percent / 100
    x = meal_cost + tip_percent + tax_percent
    print(Arredonda(x))
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
