nums = [0, 0, 1, 2, 2, 1]
n = len(nums)
start = 0
end = n - 1
i = 0

while i <= end:
    if nums[i] == 0:
        nums[start], nums[i] = nums[i], nums[start]
        start += 1
        i += 1
    elif nums[i] == 2:
        nums[end], nums[i] = nums[i], nums[end]
        end -= 1
    else:
        i += 1
print(nums)