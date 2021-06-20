                    nexts.append(root.right)
                    node = root.right.left
                    while(node):
                        nexts.append(node)
                        node = node.left
                if(root.left):
                    prevs.append(root.left)
                    node = root.left.right
                    while(node):
                        prevs.append(node)
                        node = node.right
                result.append(root.val)
                break
        nI, pI = NextIterator(nexts), PrevIterator(prevs)
        while(nI.hasNext() and pI.hasNext()):
            if(len(result) == k):
                return result
            d1, d2 = abs(nI.cur() - target), abs(pI.cur() - target)
            if(d1 < d2):
                result.append(nI.next())
            else:
                result.append(pI.next())
        while(nI.hasNext() and len(result) < k):
            result.append(nI.next())
        while(pI.hasNext() and len(result) < k):
            result.append(pI.next())
            
        return result
        
​
