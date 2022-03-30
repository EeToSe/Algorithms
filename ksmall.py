import random
class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        self.randomized_select(arr, 0, len(arr), k)
        return arr[:k]

    def randomized_select(self, arr, l, r, k):
        if l < r:
            pos = self.randomized_partition(arr,l,r)
            num = pos - l + 1
            if k < num:
                self.randomized_select(arr, l, pos - 1, k)
            else:
                self.randomized_select(arr, pos + 1, r, k - num)

    def randomized_partition(self, A, l, r):
    # pivot
        i = random.randint(l,r-1)
        A[i], A[l] = A[l], A[i]
        x = A[l]
        i = l
        for j in range(l+1, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[l], A[i] = A[i], A[l]
        return i

A = [1,2,3]
print(Solution().smallestK(A,2))