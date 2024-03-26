class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=set()
        for i in range(len(nums)):
            while nums[i]!=i+1:
                next_index=nums[i]-1
                if nums[i]!=nums[next_index]:
                    nums[i],nums[next_index]=nums[next_index],nums[i]
                else:
                    ans.add(nums[i])
                    break
        return ans
        
