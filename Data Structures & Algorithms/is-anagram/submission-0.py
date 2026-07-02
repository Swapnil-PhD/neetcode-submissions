class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for i in s:
            hash_s[i] = hash_s.get(i,0)+1
        for j in t:
            hash_t[j] = hash_t.get(j,0)+1
        if hash_t == hash_s:
            return True
        else:
            return False
        



        