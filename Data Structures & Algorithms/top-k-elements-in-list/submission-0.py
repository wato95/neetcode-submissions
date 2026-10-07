from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}

        for i in nums:
            num_counts[i] = 1 + num_counts.get(i, 0)
        
        min_heap = []

        for num, count in num_counts.items():
            heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heappop(min_heap)
            
        top_k_frequent = [pair[1] for pair in min_heap]

        return top_k_frequent
