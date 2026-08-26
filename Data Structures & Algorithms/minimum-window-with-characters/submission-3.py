class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        tCount, window = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c,0)
        
        have, need = 0, len(tCount)
        l = 0
        res, reslen = [-1,-1], float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
        
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = (r - l +1)
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""
            
            

        