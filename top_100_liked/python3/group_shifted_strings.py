class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: [])
        for s in strings:
            ll = []
            diff = ord(s[0]) - ord('a')
            for c in s:
                ll.append((ord(c) - diff + 26) % 26)
            d[tuple(ll)].append(s)
        result = []
        for k in d.keys():
            result.append(d[k])
        return result
