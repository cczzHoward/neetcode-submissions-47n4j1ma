class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # early return if len(s) != len(t)
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        i = 0

        while i < len(s):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
            i += 1
        
        return s_dict == t_dict
            
        