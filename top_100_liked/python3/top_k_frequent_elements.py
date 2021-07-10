class Solution:
    ### similar to counting sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### count the frequency
        c = {}
        for n in nums:
            if(n not in c):
                c[n] = 1
                continue
            c[n] += 1
        
        ### frequency range from 1 ~ n
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        for key in c:
            freq[c[key]].append(key)
        
        ### scan freq for the result
        result = []
        for i in range(n, -1, -1):
            if(len(freq[i]) != 0):
                for key in freq[i]:
                    result.append(key)
                    k -= 1
                    if(k == 0):
                        return result
        
        
        
        
        
        
