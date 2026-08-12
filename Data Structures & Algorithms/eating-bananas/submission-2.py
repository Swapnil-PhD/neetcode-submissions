class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        if len(piles) == 1:
            return (-(-piles[0]//h))

        piles.sort()
        k = piles[-1]

        l,r = 1, piles[-1]
        
        while l <= r:
            mid = (l+r)//2
            sums = 0
            for num in piles:
                sums += (-(-num//mid))
            if sums <= h:
                k = min(k,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return k
            

        
        

        