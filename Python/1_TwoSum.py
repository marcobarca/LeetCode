class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in dictionary:
                return [dictionary[temp], i]
            dictionary[num] = i 
