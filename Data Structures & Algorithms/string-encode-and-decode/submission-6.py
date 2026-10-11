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

        while start < len(s):
            
            while s[end] != "#":
                end += 1
            
            num = int(s[start:end])

            start = end + 1
            end = start + num
            
            ans.append(s[start:end])

            start = end
        
        return ans

            
            
            
        

