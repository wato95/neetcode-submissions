class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        n = 0
        
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                length = 1
                while (num + length) in numSet:
                    length += 1
                
                n = max(length, n)
        
        return n
                

            