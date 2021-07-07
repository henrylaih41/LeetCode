    def candy(self, ratings: List[int]) -> int:
        result = [1] ### basic case
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                result.append(result[-1]+1)
            elif(ratings[i] == ratings[i-1]):
                result.append(1)
            else:
                result.append(1)
                j = i
                while(j >= 1 and ratings[j] < ratings[j-1] and result[j-1] <= result[j]):
                    result[j-1] += 1
                    j -= 1
        return sum(result)
    
    ### faster greedy O(n) O(n) space
    ### we go on if we see continues > or < 
    def candy(self, ratings):
        result = [1]
        i = 1
        while(i < len(ratings)):
            if(ratings[i] > ratings[i-1]):
                result.append(result[-1]+1)
                i += 1
            elif(ratings[i] == ratings[i-1]):
                result.append(1)
                i += 1
            else:
                ### need to update i - 1
                count = 0
                j = i - 1
                while(j+1 < len(ratings) and ratings[j] > ratings[j+1]):
                    count += 1
                    j += 1
                # result[i-1] is the smallest possible before,
                # needs to be at least count + 1 big, we take max
                result[i-1] = max(result[i-1], count + 1)
                
                for k in range(count, 0, -1):
                    result.append(k) # set the decreasing sequence
                i = len(result)
        return sum(result)
    
    ### we use only the last two element, O(1) space
    def candy(self, ratings):
        summ = 0
