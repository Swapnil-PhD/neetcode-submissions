class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        for item in nums_set:
            if (item-1) not in nums_set:
                length = 1
                while (item+length) in nums_set:
                    length += 1
                count = max(count,length)
        
        return count
            
        