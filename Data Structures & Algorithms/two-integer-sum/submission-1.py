class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i 
        
        for j in range(len(nums)):
            comp = target - nums[j]
            if comp in hashmap and hashmap[comp] != j:
                return [j, hashmap[comp]]

        return False  

            
        