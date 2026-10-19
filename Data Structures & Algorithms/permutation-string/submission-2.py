class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = len(s1) - 1

        chars1 = [0] * 26
        chars2 = [0] * 26

        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1
        

        if chars2 == chars1:
            return True

        while r < len(s2) - 1:
            r += 1

            chars2[ord(s2[r]) - ord('a')] += 1
            chars2[ord(s2[l]) - ord('a')] -= 1

            l += 1

            if chars2 == chars1:
                return True
        
        return False
        


