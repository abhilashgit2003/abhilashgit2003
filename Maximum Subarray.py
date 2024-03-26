class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=nums[0]
        for nums in nums[1:]:
            currentsum=max(nums,currentsum+nums)
            maxsum=max(maxsum,currentsum)
        return maxsum

