class Solution:

    def encode(self, strs: List[str]) -> str:

        encode_string = ""

        for i in strs:
            tmp = str(len(i)) + "#" + i
            encode_string += tmp
        print(encode_string)
        return encode_string


    def decode(self, s: str) -> List[str]:
        
        start = 0
        end = 0
        ans = []

        while end < len(s):
            
            while s[end] != "#":
                end += 1
            
            num = int(s[start:end])
            if num == 0:
                ans.append("")
            
            else:
                ans.append(s[end + 1: end + 1 + num])
            
            start = end + 1 + num
            end = start
        
        return ans

            
            
            
        

