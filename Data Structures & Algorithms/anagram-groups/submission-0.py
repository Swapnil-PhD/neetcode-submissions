from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupdict = defaultdict(list)
        def get_idx(alp):
            return ord(alp) - ord('a')
        for s in strs:
            count = [0]*26
            for c in s:
                count[get_idx(c)] +=1
            groupdict[tuple(count)].append(s)
        
        return list(groupdict.values())



        