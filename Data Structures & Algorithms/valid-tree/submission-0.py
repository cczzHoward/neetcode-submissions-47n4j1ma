class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        # 建立 點 -> 鄰居 的 mapping
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # visit 存目前的 path
        visit = set()
        def dfs(i, prev):
            # 如果這個 node 我們走過了 (already in visit)
            # 代表 loop 了 -> False
            if i in visit:
                return False
            
            # 沒問題的話我們開始遍歷這個 node 的 neighbors
            visit.add(i)
            for j in adj[i]:
                # 跳過前一個 node, 不遍歷到他 (沒有這個會無限迴圈)
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            # 都沒有遇到有問題的 node 代表沒問題 -> True
            return True
        
        # n 跟我們 visit 數量一樣   -> valid tree
        # n 跟我們 visit 數量不一樣 -> 代表不是所有 node 連在一起 -> invalid tree
        return dfs(0, -1) and n == len(visit)