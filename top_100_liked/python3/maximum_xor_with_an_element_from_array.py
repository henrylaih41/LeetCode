                    ### choose bit
                    else:
                        curr = curr[bit]
            result.append(maxx)
        return result
​
    def maximizeXor(self, nums, queries):
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        nums.sort()
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: x[1])
        i, j = 0, 0
        result = [None] * len(queries)
        while(j < len(queries)):
            ### insert
            while(i < len(nums) and queries[j][1] >= nums[i]):
                arr = [1 if (nums[i] & 1 << k) else 0 for k in range(31, -1, -1)]
                reduce(dict.__getitem__, arr, trie)
                i += 1
            x, m, pos = queries[j]
            ### trie is still empty
            if(0 not in trie and 1 not in trie):
                result[pos] = -1
            else:
                curr = trie
                maxx = 0
                for k in range(31, -1, -1):
                    acc = 1 << k
                    bit = 1 if (x & acc) else 0
                    inv_bit = 1 - bit
                    ### we can choose the best 
                    if(inv_bit in curr):
                        maxx += acc
                        curr = curr[inv_bit]
                    ### choose bit
                    else:
                        curr = curr[bit]
                result[pos] = maxx
            j += 1
        return result
​
