from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for char in s:
            count_s[char] +=1
        for j in t:
            count_t[j] +=1
        if count_s == count_t:
            return True
        
        return False


        
        