class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        res = [0]*len(nums)
        count = 0
        prod = 1
        for n in nums:
            if n == 0:
                count +=1
            else: 
                prod *= n
        
        if count > 1:
            return res
        elif count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
        else:
            for i in range(len(nums)):
                res[i] = prod // nums[i]
        
        return res
                    
            
                


            