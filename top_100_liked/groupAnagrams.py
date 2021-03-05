class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {}
        result    = []
        for s in strs:
            count = [0] * 26 # 26 lowercase alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count) # make into tuple to be hashable
            if(count not in group_map):
                group_map[count] = len(result)
                result.append([s])
            else:
                group_id = group_map[count]
                result[group_id].append(s)
        return result

