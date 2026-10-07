class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        longest = 1

        num_set = set(nums)

        for i in nums:
            if i-1 in num_set:
                continue
            else:
                j = 1
                tracker = 1
                stop = False
                while not stop:
                    if i + j in num_set:
                        j += 1
                    else:
                        stop = True
                
                if j >= longest:
                    longest = j
                    
        return longest
                
            


            