#!/bin/python3
def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        # i,j,k used to index L,R and arr
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        # Supplement
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

######### This is the first attempt
# def mergeSort(arr):
#     n = len(arr)
#     if n == 1:
#         return arr
#     mid = n//2
#     L = arr[:mid]
#     R = arr[mid:]
#     Ls = mergeSort(L)
#     Rs = mergeSort(R)
#     i, j = 0,0
#     # We create a new array here, which is unnecessary
#     sorted_arr = []
#     while i < len(Ls) or j < len(Rs):
#         if Ls[i] < Rs[j]:
#             sorted_arr.append(Ls[i])
#             if (i+1) >= len(Ls):
#                 sorted_arr = sorted_arr + Rs[j:]
#                 break
#             else:
#                 i += 1
#
#         else:
#             sorted_arr.append(Rs[j])
#             if (j + 1) >= len(Rs):
#                 sorted_arr = sorted_arr + Ls[i:]
#                 break
#             else:
#                 j += 1
#
#     return sorted_arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    mergeSort(arr)
    for i in arr:
        print(i, end=' ')