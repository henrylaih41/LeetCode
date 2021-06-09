class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        prefix_cand = defaultdict(lambda: []) ### (tac)[p]cat
        suffix_cand = defaultdict(lambda: [])
        result = set()
        for i, w in enumerate(words):
            prefix_cand[w[::-1]].append(i)
            suffix_cand[w[::-1]].append(i)
            for l in range(len(w)):
                if(w[:l+1] == w[:l+1][::-1]):
                    prefix_cand[w[l+1:][::-1]].append(i)
                if(w[l:] == w[l:][::-1]):
                    suffix_cand[w[:l][::-1]].append(i)
        for j, w in enumerate(words):
            if(w in prefix_cand):
                for i in prefix_cand[w]:
                    if(i == j):
                        continue
                    result.add((j, i))
            if(w in suffix_cand):
                for i in suffix_cand[w]:
                    if(i == j):
                        continue
                    result.add((i, j))
        
        return list(result)
    
        
