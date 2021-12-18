def match(text, pattern):
    n = len(text)
    m = len(pattern)
    p = 31
    pp = p ** (m - 1)

    rolling_sum = 0
    for i in range(m):
        rolling_sum = rolling_sum * p + ord(text[i])
    pattern_sum = 0
    for i in range(m):
        pattern_sum = pattern_sum * p + ord(pattern[i])
    if pattern_sum == rolling_sum:
        return print(0)

    for i in range(m, n):
        rolling_sum -= ord(text[i - m]) * pp
        rolling_sum = ord(text[i]) + rolling_sum * p
        if rolling_sum == pattern_sum and pattern == text[i - m + 1:i + 1]:
            print(i - m + 1)


if __name__ == "__main__":
    text = "ageeks for geeks"
    pattern = "geeks"
    match(text, pattern)
