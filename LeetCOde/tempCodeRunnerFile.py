i = 0 
    while i != len(s) + 1:
        j = i + 1
        while j != len(s) + 1 and ((j - i) <= len(s)//2 + 1):
            if s[i:j] == s[j + j - i - 1:i + 1:-1]:
                if len(max) < len(s[i:j + j - i]):
                    max = (s[i:j + j - i])
            if s[i:j] == s[j + j - i - 1:i:-1]:
                if len(max) < len(s[i:j + j - i]):
                    max = (s[i:j + j - i])
            if s[i:j] ==  s[j + j - i:j:-1]:
                if len(max) < len(s[i:j + j - i]):
                    max = (s[i:j + j - i + 1])
            j += 1
        i += 1
    return max 