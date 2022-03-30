class Solution(object):
    # Median of two sorted arrays of equal length n
    def Median_arrays(self, X, Y, n):
        if n == 1:
            return (X[0]+Y[0])/2
        elif n == 2:
            return (max(X[0],Y[0])+min(X[1],Y[1]))/2
        else:
            m1 = self.median(X,n)
            m2 = self.median(Y,n)
            if m1 == m2:
                return m1

            elif m1 > m2:
                if n % 2 == 0:
                    return self.Median_arrays(X[: n//2], Y[n//2: ], n//2)
                else:
                    return self.Median_arrays(X[: n//2+1], Y[n//2: ], n//2+1)
            else:
                if n % 2 == 0:
                    return self.Median_arrays(X[n//2: ], Y[: n//2], n//2)
                else:
                    return self.Median_arrays(X[n//2: ], Y[: n//2+1], n//2+1)

    def median(self, arr, n):
        if n % 2 == 0:
            return (arr[n//2] + arr[n//2-1])/2
        else:
            return arr[n//2]

X = [2, 13, 17, 30, 45]
Y = [1, 12, 15, 26, 38]
n = len(X)
print(Solution().Median_arrays(X, Y, n))