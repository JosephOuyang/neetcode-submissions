class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my first idea (brute force)
        result = []
        for i in range(len(nums)):
            currProduct = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    currProduct *= nums[j]
            result.append(currProduct)
        return result
                

        