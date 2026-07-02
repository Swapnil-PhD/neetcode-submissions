from collections import defaultdict
class Solution:
    def get_ord(self, word):
        lis = [0]*26
        for i in word:
            lis[ord(i)-ord('a')] +=1
        
        return tuple(lis)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = defaultdict(list)

        for j in strs:
            key = self.get_ord(j)
            diction[key].append(j)

        return list(diction.values())


        