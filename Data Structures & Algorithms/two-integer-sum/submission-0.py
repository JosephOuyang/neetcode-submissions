class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracked = dict()
        for i in range(len(nums)):
            currNum = nums[i]
            complement = target - currNum
            if complement in tracked:
                return [tracked[complement], i]
            tracked[currNum] = i
            
        