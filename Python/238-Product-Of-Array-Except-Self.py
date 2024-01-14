class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_vals = tuple(nums)
        prefix = 1
        for i in range(len(nums)):
            nums[i] = prefix
            prefix *= nums_vals[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            nums[i] *= postfix
            postfix *= nums_vals[i]
        return nums