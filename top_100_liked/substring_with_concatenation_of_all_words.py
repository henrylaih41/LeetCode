from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = set()
        ss, step = defaultdict(lambda: 0), len(words[0])
        count = 0
        for w in words:
            ss[w] += 1
            count += 1
        for i in range(len(words[0])):
            self.find(s, ss, count, result, i, step)
        return list(result)
    
    def find(self, s, ss, count, result, start, step):
        head, tail = start, start
        while(tail < len(s)):
            cand = s[tail:tail+step]
            if(ss.get(cand, 0) != 0):
                ss[cand] -= 1
                count -= 1
                tail = tail + step
            elif(head == tail):
                tail = tail + step
                head = head + step
            else:
                ss[s[head:head+step]] += 1
                count += 1
                head = head + step
                
            if(count == 0):
                result.add(head)
                ss[s[head:head+step]] += 1
                count += 1
                head = head + step
        ### maintain ss
        while(head != tail):
