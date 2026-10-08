class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        groups = {}
        
        for word in strs:
            chars = [0] * 26
            for j in word:
                chars[ord(j) - ord('a')] += 1
            chars = tuple(chars)
            sub_group = groups.get(chars, 0)
            if sub_group == 0:
                groups[chars] = [word]
            else:
                sub_group.append(word)
                groups[chars] = sub_group
        
        ans = [group for _, group in groups.items()]
        return ans

                

        