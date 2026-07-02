from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        for i in count_s.keys():
            if count_s[i] != count_t[i] or i not in count_t:
                return False
        
        return True

        

        