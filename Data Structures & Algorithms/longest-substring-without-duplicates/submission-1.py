class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        used = set()
        max_length = 1

        l, r = 0, 1

        while r < n:
            used.add(s[l])

            if s[r] in used:
                l += 1
                r = l + 1
                used = set()

            else:
                used.add(s[r])
                r += 1
                length = r - l
                max_length = max(length, max_length)
        
        return max_length

