class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[x[0]**2 + x[1]**2, x[0], x[1]] for x in points]
        heapq.heapify(dist)
        res = []

        while k > 0:
            distance, x, y = heapq.heappop(dist)
            res.append([x,y])
            k-= 1
        
        return res