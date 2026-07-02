from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort_count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
        return list(sort_count.keys())[:k]