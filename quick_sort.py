def quick_sort(A, p, r):
    # pivot
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)

def partition(A, p, q):
    # pivot
    x = A[p]
    i = p
    for j in range(p+1, q):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i

if __name__ == '__main__':
    A = [6,10,13,5,8,3,2,11]
    quick_sort(A,0,len(A))
    for i in A:
        print(i, end=' ')