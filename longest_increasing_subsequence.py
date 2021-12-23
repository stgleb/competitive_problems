def longest_increasing_subsequence(a):
    n = len(a)
    prefix = [0 for _ in range(n)]
    max_len = 0
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                prefix[i] = max(prefix[i], prefix[j] + 1)
                max_len = max(max_len, prefix[i])
    return max_len


if __name__ == "__main__":
    arr = [2, 1, 5, -7, 4, 6, 7, 3]
    print(longest_increasing_subsequence(arr))
