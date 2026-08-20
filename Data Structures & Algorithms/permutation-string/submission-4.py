from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        s2Count = Counter(s2[:len(s1)])

        need = len(s1Count)
        matches = 0
        for ch in s1Count:
            if s1Count[ch] == s2Count.get(ch, 0):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True

            add_ch = s2[r]
            s2Count[add_ch] += 1
            if add_ch in s1Count:
                if s1Count[add_ch] == s2Count[add_ch]:
                    matches += 1
                elif s1Count[add_ch] + 1 == s2Count[add_ch]:
                    matches -= 1

            rem_ch = s2[l]
            s2Count[rem_ch] -= 1
            if rem_ch in s1Count:
                if s1Count[rem_ch] == s2Count[rem_ch]:
                    matches += 1
                elif s1Count[rem_ch] - 1 == s2Count[rem_ch]:
                    matches -= 1

            l += 1

        return matches == need