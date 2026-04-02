class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_char = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def bt(i, curr_str):
            # 如果 current_string 長度 = digit 長度 => 找完了
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for c in digit_to_char[digits[i]]:
                bt(i+1, curr_str+c)
            
        if digits == "":
            return res
        
        bt(0, "")
        return res

        