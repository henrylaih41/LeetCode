from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ### sort all points by x and add key
        ### maintain a alive array to see whether the key in heap is valid
        ### for each point 
            ### if p.h > heap.max: push to result
            ### if alive[p] == 0 add to heap alive[p] = 1
            ### else alive[p] = 0
            ### while(heap.max.key not alive): pop heap
            
        alive = [0] * len(buildings)
        heap, points, result = [], [], []
        for i, (x1, x2, h) in enumerate(buildings):
            ### First we sort by x cordinates
            ### Second we want the start points in the front of end points
            ### Third for start points we want high points to be handle first
            ### And for end points we want low points to be handle first
            points.append((x1, -1, -h, i))
            points.append((x2, 1, h, i))
        points.sort()
        for x, s, h, i in points:
            h *= s
            ### this is always the start points
            ### the start points is handled high to low, so it is
            ### safe to push into result if len(heap) == 0
            ### since all preceding points would be lower
            if(len(heap) == 0 or h > -heap[0][0]):
                result.append([x, h])
            
            if(alive[i] == 0):
                heappush(heap, (-h, i))
                alive[i] = 1
            else:
                alive[i] = 0
                while(len(heap) and alive[heap[0][1]] == 0):
                    heappop(heap)
                if(len(heap) == 0):
                    result.append([x, 0])
                elif(h > -heap[0][0]):
                    result.append([x, -heap[0][0]])
        
        return result
