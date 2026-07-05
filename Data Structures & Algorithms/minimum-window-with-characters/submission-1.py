class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s="ADOBECODEBANC"
        # t="ABC"

        # edge case
        if t == "": return ""

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(t)):
            t_dict[t[i]] += 1
        
        have, need = 0, len(t_dict)
        # save res's left&right pointer and tranfer it at the end of function
        res, res_length = [0, 0], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            s_dict[c] += 1

            # need char c and reach amount of char c
            if c in t_dict and s_dict[c] == t_dict[c]:
                have += 1

                # reach rule we need -> update res if we find shorter answer
                while have == need:
                    if (right-left+1) < res_length:
                        res = [left, right]
                        res_length = right-left+1
                    
                    s_dict[s[left]] -= 1
                    if s[left] in t_dict and s_dict[s[left]] < t_dict[s[left]]:
                        have -= 1
                    
                    left += 1
        
        # transfer pointer to real answer
        left, right = res
        return s[left:right+1] if res_length != float("inf") else ""

