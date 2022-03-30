#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
        key = i
        while key > 0:
            if arr[key-1] <= arr[key]:
                break
            else:
                tmp = arr[key-1]
                arr[key-1] = arr[key]
                arr[key] = tmp
                key -= 1
        for i in arr:
            print(i, end=' ')
        print(' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
