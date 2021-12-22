def distance_rec(s1, s2):
    if s1 == "" and s2 == "":
        return 0
    if s1 == "" or s2 == "":
        return max(len(s1), len(s2))
    if s1[0] == s2[0]:
        return distance_rec(s1[1:], s2[1:])
    return min(distance_rec(s1, s2[1:]), distance_rec(s1[1:], s2), distance_rec(s1[1:], s2[1:])) + 1


def distance_dp(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[n][m]


if __name__ == "__main__":
    print(distance_rec("barbaris", "baracuda"))
    print(distance_dp("barbaris", "baracuda"))

