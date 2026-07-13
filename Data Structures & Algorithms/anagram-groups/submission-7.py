class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            ans[key].append(string)

        return list(ans.values())



























