class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for i in nums:
            if i == 0:
                zero_cnt +=1
            else:
                prod *= i
        
        result = [0]*(len(nums))
        if zero_cnt > 1: return result
        if zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] != 0: result[i] = 0
                else: result[i] =prod
        else:
            for i in range(len(nums)):
                result[i] = prod//nums[i]
        return result