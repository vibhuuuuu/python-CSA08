def findKthNumber(M, N, K):
    def count_less_equal(x):
        count = 0
        for i in range(1, M + 1):
            count += min(x // i, N)
        return count
    
    left, right = 1, M * N
    
    while left < right:
        mid = left + (right - left) // 2
        if count_less_equal(mid) < K:
            left = mid + 1
        else:
            right = mid
    
    return left
