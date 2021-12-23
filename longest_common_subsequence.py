def longest_common_subsequence_rec(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[0] == s2[0]:
        return longest_common_subsequence_rec(s1[1:], s2[1:]) + 1
    return max(longest_common_subsequence_rec(s1, s2[1:]), longest_common_subsequence_rec(s1[1:], s2))


def longest_common_subsequence_dp(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    sol = []
    i, j = n, m
    while i > 0 and j > 0 and dp[i][j] != 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            sol.append(s1[i])
            i -= 1
            j -= 1

    return sol


if __name__ == "__main__":
    print(longest_common_subsequence_rec("abcdae", "aedbea"))
    print(longest_common_subsequence_dp("abcdae", "aedbea"))

