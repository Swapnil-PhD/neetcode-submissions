class Solution:
    def isPalindrome(self, s: str) -> bool:
        #x1 = s.lower().split()
        #s = "".join(s.lower().split())
        s1 = "".join([i for i in s if i.isalnum()])
        s1 = s1.lower()
        n = len(s1)
        l = 0 
        r = n-1
        while l <= r:
            if s1[l] != s1[r]:
                return False
            else:
                l +=1
                r -=1

        return True 

        