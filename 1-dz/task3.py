def longestCommonPrefix(x):
    check_word = x[0].strip()
    for i in range(1, len(check_word)+1):
        for w in x:
            w = w.strip()
            if check_word[:i] != w[:i]:
                return check_word[:i-1]
    return check_word
if __name__ == "__main__":
    print(longestCommonPrefix(["      flower","  flow"," flight", "flight    "]))

