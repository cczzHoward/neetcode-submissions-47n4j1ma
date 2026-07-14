class Solution:
    def encode(self, strs: List[str]) -> str:
        # ["Hello", "everyone"] -> "5#Hello8#everyone":
        encode_str = ""
        
        for string in strs:
            encode_str += str(len(string)) + '#' + string

        return encode_str

    def decode(self, s: str) -> List[str]:
        # "5#Hello8#everyone" -> ["Hello", "everyone"]
        decode_list = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            decode_list.append(s[i:j])
            
            i = j


        return decode_list
