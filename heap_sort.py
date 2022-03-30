def Heap_Sort(arr):
    # produces a max heep from an unordered array
    n = len(arr)
    # Build_Max_Heap
    for i in range(n//2, -1, -1):
        Max_Heapify(arr, n, i)

    # "pop-up"
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        Max_Heapify(arr, i, 0)

def Max_Heapify(arr, n, i):
    # n - heap-size
    # i - root
    left = 2 * i + 1
    right = 2 * (i+1)
    if left <= n - 1 and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right <= n - 1 and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        Max_Heapify(arr, n, largest)

# def Min_Heapify(A, i):
#     if (i <= len(A)//2):
#         left = 2 * i + 1
#         right = 2 * (i+1)
#         if left <= len(A) - 1 and A[left] < A[i]:
#             smallest = left
#         else:
#             smallest = i
#         if right <= len(A) - 1 and A[right] < A[smallest]:
#             smallest = right
#         if smallest != i:
#             A[smallest], A[i] = A[i], A[smallest]
#             Min_Heapify(A, smallest)


if __name__ == '__main__':
    A = [4,1,3,2,16,9,10,14,8,7]
    Heap_Sort(A)
    print(A)
