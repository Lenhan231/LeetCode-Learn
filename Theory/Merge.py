nums1 = [1,2]
nums2 = [3,4]
def merge(nums1, nums2):
    lst = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            lst.append(nums1[i])
            i += 1
        else:
            lst.append(nums2[j])
            j += 1
    while j < len(nums2):
        lst.append(nums2[j])
        j += 1
    while i < len(nums1):
        lst.append(nums1[i])
        i += 1
    return lst

result = merge(nums1, nums2)
meadian = float()
if int(len(result) - 1) % 2 == 0:
    print(result[int((len(result) - 1)/2)])
else:
    meadian = (result[int((len(result) - 1)/2)] + result[int((len(result) - 1)/2) + 1])/2

print(meadian)
      
