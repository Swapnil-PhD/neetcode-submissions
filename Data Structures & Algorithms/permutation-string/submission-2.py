class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        s1_count = {}
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)

        l = 0
        for r in range(len(s1), len(s2)+1):
            counts = {}
            for j in range(l, r):
                counts[s2[j]] = 1 + counts.get(s2[j],0)
            
            if counts == s1_count:
                return True
            
            l += 1
        
        return False 
        
        