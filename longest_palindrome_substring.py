def longest_palindromic_substring(text):
    n = len(text)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
        if i + 1 < n and text[i] == text[i + 1]:
            dp[i][i + 1] = True

    k = 2
    max_len = 0
    while k < n:
        i = 0
        j = k
        while j < n:
            if text[i] == text[j] and dp[i + 1][j - 1]:
                max_len = max(max_len, j - i)
                dp[i][j] = True
            i += 1
            j += 1
        k += 1
    return max_len + 1


if __name__ == "__main__":
    text = "abcbabcba"
    print(longest_palindromic_substring(text))
