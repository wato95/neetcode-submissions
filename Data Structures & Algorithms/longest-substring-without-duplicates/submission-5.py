class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0

        length = 0
        chars = set()

        while r < len(s):
            if s[r] in chars:
                length = max(length, len(chars))
                chars.remove(s[l])
                l += 1
            else:
                chars.add(s[r])
                r += 1
        
        return max(length, len(chars))


