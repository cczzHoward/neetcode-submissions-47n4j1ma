class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 這題好像跟是 #UnionFind
        # 但我看了影片還是不太懂, 第二次看的話要多花時間
        par = [i for i in range(n)]
        rank = [1] * n
    
        def find(n1):
            res = n1

            while res != par[res]:
                # 一個優化方案(讓 linked_list 更短)
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
        
            if p1 == p2:
                return 0
            
            # p2 比較大坨 -> p1 合併進 p2
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            # p1 比較大坨 -> p2 合併進 p1
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res