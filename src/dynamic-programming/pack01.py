def pack1(w, v, C):
    dp = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
    return dp[-1][-1]

if __name__ == '__main__':
    c = int(input())
    w = list(map(lambda x:int(x),list(input().split(','))))
    v = list(map(lambda x:int(x),list(input().split(','))))
    print(pack1(w, v, c))
