class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in maps and maps[comp] != i:
                return [i,maps[comp]]
            

        