
# this is some python comments

# this is another one

# and a third one

class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
result = sol.twoSum(nums, target)
print(result)

