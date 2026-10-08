class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        groups = defaultdict(list)
        
        for word in strs:
            chars = [0] * 26

            for j in word:
                chars[ord(j) - ord('a')] += 1

            groups[tuple(chars)].append(word)
        
        return list(groups.values())

                

        