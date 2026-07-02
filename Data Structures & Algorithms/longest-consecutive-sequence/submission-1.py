class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        nums = sorted(nums)
        l = 0
        current_len = 1
        max_len = 1

        while l<len(nums)-1:
            if nums[l+1] - nums[l] > 1:
                l +=1
                current_len = 1
            elif nums[l+1] - nums[l] ==1:
                current_len +=1
                max_len = max(current_len,max_len)
                l +=1
            elif nums[l+1] - nums[l] ==0:
                l +=1

        return max_len 
            
        