class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque()

        time = 1

        while True:
            if maxHeap:
                task = heapq.heappop(maxHeap)
                if task < -1:
                    q.append([task + 1, time + n])

            if q and q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])
            
            if not maxHeap and not q:
                return time

            time += 1


