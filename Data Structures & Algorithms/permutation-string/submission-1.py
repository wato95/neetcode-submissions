class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_freq = [0] * 26
        
        for i in s1:
            s1_freq[ord(i) - ord("a")] += 1
        
        l, r = 0, len(s1)

        print(s1_freq)

        while r <= len(s2):
            s2_freq = [0] * 26
            for i in s2[l:r]:
                s2_freq[ord(i) - ord("a")] += 1

            print(s2[l:r])
            print(s2_freq)

            if s2_freq == s1_freq:
                return True
            
            else:
                l += 1
                r += 1
        
        return False