class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = defaultdict(list)

        for string in strs:
            # cat -> [a, c, t] -> act
            key = "".join(sorted(string))
            string_dict[key].append(string)
        
        return list(string_dict.values())