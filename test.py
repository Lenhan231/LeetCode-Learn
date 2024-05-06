k = int(input())
h = dict()
for i in range(1, int((2*k - 2) / 3)): # n bigger
    carry = (2*k - i - 1)/(2*i + 1) # calculate m 
    if (carry*10)%10 == 0 and i > carry and carry != 0:  # check m if int 
            h[carry - i] = f"{int(carry)} {i}" # hash 
if h: # empty list 
    print(h[min(h.keys())])
else:
    print("-1 -1")
