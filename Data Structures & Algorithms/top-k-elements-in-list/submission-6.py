class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        for num, count in counts.items():
            freq[count].append(num)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans