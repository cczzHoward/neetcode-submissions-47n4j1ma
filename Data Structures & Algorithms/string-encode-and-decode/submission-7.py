class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "everyone"] -> "5#Hello8#everyone"
        encode_string = ""

        for string in strs:
            encode_string += str(len(string)) + '#' + string
        
        return encode_string


    def decode(self, s: str) -> List[str]:
        # "5#Hello8#everyone" -> ["Hello", "everyone"]
        decode_string_list = []

        i = 0
        while i < len(s):
            # caculate string length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # get the string with length
            i = j + 1
            j = i + length
            decode_string_list.append(s[i:j])

            # prepare for next iterate
            i = j

        return decode_string_list

            
            