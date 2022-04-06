class Solution(object):
    def sum_A(self, A, l, r):
        res = 0
        for i in range(l, r + 1):
            res += A[i]
        return res

    def min_maximums(self, A, N, B):
        if N == 1:
            return A[1]

        if N > 1:
            # A[0] = 0 for auxiliary
            A.insert(0,0)
            r = [2**40 for _ in range(N+1)]
            r[0] = 0
            r[1] = A[1]
            # compute r[2]...r[N]
            for i in range(2, N+1):
                j = i
                # move index j = i to the left
                while j >= 1 and self.sum_A(A, j, i) <= B:
                    r[i] = min(r[i], r[j-1] + max(A[j:i+1]))
                    j -= 1
            return r[N]

A = [2,2,2,8,1,8,2,1]
print(Solution().min_maximums(A,8,17))
