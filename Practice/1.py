def twoSum(nums, target):
        hashtable = dict()
        for i in range(len(nums)):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = i
        print(hashtable)
        for i in range(len(nums)):
        
            if (target - nums[i]) in hashtable and hashtable[target - nums[i]] != i:
                return i, hashtable[target - nums[i]]
nums = [3,2,4]
target = 6
print(twoSum(nums, target)) 