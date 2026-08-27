from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        res = []
        q   = deque()

        l, r = 0, 0
        while r < len(nums):
            #if not q:
            #    q.append(r)
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res
