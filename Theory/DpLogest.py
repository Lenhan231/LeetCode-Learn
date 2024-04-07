'''def longest_increasing_subsequence(A):
    n = len(A)
    L = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] <= A[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1

    return max(L)'''

# Example usage:
a = [3, 4, 2, 8, 10, 5, 1]
dp = [1]*len(a)
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            dp[i] = dp[j] + 1
