class Solution(object):
    def sum_A(self, A, l, r):
        res = 0
        for i in range(l, r+1):
            res += A[i]
        return res

    def Bottom_Up_Mul_Add(self, A, N, K):
        if K == 0:
            sumA = 0
            for i in A:
                sumA = sumA + i
            return sumA
        # init K = 0, i.e. without Multiplication
        r = [[0] * (K+1) for _ in range(N+1)]
        r[1][0] = 1
        for ni in range(2, N+1):
            r[ni][0] = r[ni-1][0] + ni

        # ki: # of Mul; ni: first ni numbers; nj: Mul insertion position
        for ki in range(1, K+1):
            for ni in range(ki+1, N+1):
                for nj in range(ki, ni):
                    r[ni][ki] = max(r[ni][ki], r[nj][ki-1]*self.sum_A(A,nj,ni-1))
        return r[N][K]

A = [1,2,3,4,5,6]
print(Solution().Bottom_Up_Mul_Add(A, 6, 3))