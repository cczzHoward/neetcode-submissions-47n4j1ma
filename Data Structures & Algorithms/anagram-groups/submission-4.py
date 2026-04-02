class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # 把 act, cat 透過 sorted() 拆成 ['a', 'c', 't']
            # 再用 "".join() 變成 "act"
            # 用 "act" 為 key 把它們分到同一個 array 中
            key = "".join(sorted(s))
            ans[key].append(s)

        # 回傳每個 subarray 的 value
        return list(ans.values())
