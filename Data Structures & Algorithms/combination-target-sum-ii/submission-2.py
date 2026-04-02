class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def bt(i, sub_sum):
            if sub_sum == target:
                res.append(subset.copy())
                return
            
            if sub_sum >= target or i >= len(candidates):
                return

            subset.append(candidates[i])
            bt(i + 1, sub_sum + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            bt(i + 1, sub_sum)

        bt(0, 0)
        return res