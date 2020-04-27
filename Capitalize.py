#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)

    for i in range(0,len(s)) :
        s[0] = s[0].upper()
        if s[i] == " " :
            s[i+1] = s[i+1].upper()
    return(''.join(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
