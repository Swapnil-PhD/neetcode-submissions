class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_join = ''.join(char.lower() for char in s if char.isalnum())
        #length = len(s_join)
        l , r = 0, (len(s_join)-1)

        while l <= r:
            if s_join[l] != s_join[r]:
                return False
            
            l +=1
            r -=1
        
        return True