import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] -=1
            else:
                count[i] = -1


        heap = []
        for key, val in count.items():
            heapq.heappush(heap,(val,key))

        kfrequent = []
        for j in range(k):
            large = heapq.heappop(heap)
            kfrequent.append(large[1])
        
        return kfrequent
        