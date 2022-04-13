class Solution(object):
    def sortArray(self, nums):
        k = max(nums)
        return self.countingSort(nums, k)

    # def countingSort(self, A, k):
    """
    MIT version
    """
    #     B = [0] * len(A)
    #     C = [0] * (k+1)
    #     for x in A:
    #         C[x] += 1
    #     for i in range(1,k+1,1):
    #         C[i] += C[i-1]
    #     for j in range(len(A)-1,-1,-1):
    #         B[C[A[j]]-1] = A[j]
    #         C[A[j]] -= 1
    #     return B

    def countingSort(self, A, k):
        """
        C store the frequencies of each element in A
        """
        B = [0] * len(A)
        C = [0] * (k+1)
        for x in A:
            C[x] += 1
        j = 0
        for i in range(k+1):
            tmp = C[i]
            while (tmp > 0):
                B[j] = i
                tmp -= 1
                j += 1
        return B,C





# print(Solution().sortArray([2,5,3,0,2,3,0,3]))