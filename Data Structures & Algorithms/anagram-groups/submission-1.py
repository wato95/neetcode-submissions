class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) < 2:
            return [strs]
        

        anagram_count = {}

        for i in strs:
            i_count = [0] * 26
            for j in i:
                i_count[ord(j) - ord("a")] += 1
            
            index = tuple(i_count)

            if index not in anagram_count.keys():
                anagram_count[index] = [i]
            else:
                anagram_count[index].append(i)
        
        return anagram_count.values()

