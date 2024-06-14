nums1 = [1,2]
nums2 = [3,4]
def func(nums1, nums2):
    num3 = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            num3.append(nums1.pop(0))
        else:
            num3.append(nums2.pop(0))        
    while nums1:
        num3.append(nums1.pop(0))
    while nums2:
        num3.append(nums2.pop(0))
    print(num3)
    
    if (len(num3) - 1)  % 2 == 0:
        return (num3[(len(num3)-1) // 2])
    else:
        return ((num3[len(num3)//2] + num3[(len(num3)//2) - 1])/2)
print(func(nums1, nums2))

