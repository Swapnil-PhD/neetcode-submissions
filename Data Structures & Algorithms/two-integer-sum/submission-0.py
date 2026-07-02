class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i, num in enumerate(nums):
            comple = target - num
            if comple in hashmap and hashmap[comple] != i:
                return [i,hashmap[comple]]
            