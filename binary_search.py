#!/bin/python3
def binary_search(x,arr,low,high):
    while low <= high:
        mid = (low+high) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid -1
            return binary_search(x,arr,low,high)
        else:
            low = mid + 1
            return binary_search(x,arr,low,high)
    return -1

if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().strip().split(' ')))
    # x = int(input())
    index = binary_search(1,[1,2,3,4],0,3)
    print(index)