class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        need = Counter(p)
        cur, lo = 0, 0
        ret = []

        for i, c in enumerate(s):
            need[c] -= 1
            cur += 1
            while need[c] < 0:
                need[s[lo]] += 1
                lo += 1
                cur -= 1
            if cur == len(p):
                ret.append(lo)
        return ret
