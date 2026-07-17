#from collections import Counter
from collections import defaultdict
class Solution:
    def get_ord(self,char):
        return ord(char) - ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            mapping = [0]*26
            for char in s:
                mapping[self.get_ord(char)] +=1
            anagrams[tuple(mapping)].append(s)
        
        return list(anagrams.values())


        