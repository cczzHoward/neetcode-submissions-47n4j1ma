class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string = ""
        for string in strs:
            output_string += str(len(string)) + '#' + string
        
        return output_string

    def decode(self, s: str) -> List[str]:
        output_list = []

        i = 0
        # 5#Hello5#World
        while i < len(s):
            # caculate string length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            
            # get the string with length
            i = j + 1
            j = i + length
            output_list.append(s[i:j])

            # prepare for next iterate
            i = j

        return output_list