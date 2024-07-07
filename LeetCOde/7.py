s = "-042"
k = 0
s = s.strip()
if s[0] == '-':
    for i in range(1,len(s)):
        if s[i] == 0:
            pass
        elif s[i] in '123456789':
            k = i
        else:
            break
else:
    for i in range(len(s)):
        if s[i] == 0:
            pass
        elif s[i] in '123456789':
            k = i
        else:
            break


if k == 0 and s[0] not in '-123456789':
    print(k)
if s[k] in '123456789':
    print(s[:k+1])
else:
    print(s[:k])

