class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        
        l,r = 0, n-1
        mid = (l+r)//2
        if nums[mid] < nums[-1]:
            return self.findMin(nums[0:mid+1])
        if nums[mid] > nums[-1]:
            return self.findMin(nums[mid+1:])
        
            
        