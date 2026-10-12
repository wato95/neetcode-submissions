class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for i in strs:
            chars = [0] * 26
            for j in i:
                chars[ord(j) - ord('a')] += 1
            
            groups[tuple(chars)].append(i)
        
        return list(groups.values())
