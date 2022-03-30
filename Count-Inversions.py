class Solution(object):
    def reversePairs(self, nums):
        n = len(nums)
        return self.Count_Inversions(nums, 0, n-1)

    def Count_Inversions(self, A, l, r):
        if l < r:
            mid = (l + r)//2
            left = self.Count_Inversions(A, l, mid)
            right = self.Count_Inversions(A, mid+1, r)
            inv = self.Merge_Sort_Count(A, l, mid, r) + left +right
            return inv
        return 0

    def Merge_Sort_Count(self, A, l, mid, r):
        inv = 0
        L = A[l:mid+1]
        R = A[mid+1:r+1]
        i,j,k = 0,0,l
        while i != mid-l+1 and j != r-mid:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
                inv += mid-l-i+1
            k += 1
        if i == mid - l +1:
            for m in range(j, r-mid):
                A[k] = R[m]
                k += 1
        if j == r-mid:
            for m in range(i, mid-l+1):
                A[k] = L[m]
                #inv += r-mid -1
                k += 1
        return inv
A = [7,5,6,4,2]
print(Solution().Count_Inversions(A,0,len(A)-1))
print(A)
