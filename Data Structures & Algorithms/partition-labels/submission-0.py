class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        # 創建 字母 -> 最後一個出現的 index 的 mapping
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        # size -> 現在的 partition size
        # end -> 現在這個 partition 的 end index
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            # 抵達這個 partition 的 end index
            # 更新 res, size
            if i == end:
                res.append(size)
                size = 0
        
        return res