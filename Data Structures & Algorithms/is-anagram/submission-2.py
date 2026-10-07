class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for i in s:
            if s_dict.get(i,0) == 0:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        
        for j in t:
            if t_dict.get(j,0) == 0:
                t_dict[j] = 1
            else:
                t_dict[j] += 1

        for letter, num in s_dict.items():
            if t_dict.get(letter, 0) == num:
                pass
            else:
                return False
        
        return True
