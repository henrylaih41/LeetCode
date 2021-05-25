class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #citations.sort(key=lambda x : -x) O(nlogn)
        self.countSort(citations) # O(n)
        for i in range(len(citations)-1, -1, -1):
            if(citations[i] >= i+1 and (i == len(citations)-1 or citations[i+1] <= i+1)):
                return i+1
        return 0
    
    def countSort(self, citations):
        count = [0]*(len(citations)+1)
        for n in citations:
            if(n >= len(citations)):
                count[len(citations)] += 1
            else:
                count[n] += 1
        j = len(citations)-1
        for i in range(len(count)):
            for _ in range(count[i]):
                citations[j] = i
                j -= 1
