class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 這題也是 UnionFind, 但是看影片更不懂了
        # 一定視需要再回來複習的一題題目
        # 大概理解 20%(UnionFind運作模式) 吧
        # rank list 的維護不太知道是在幹嘛
        N = len(edges)
        # par: 這個 node 的 root 是誰
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        # 找到 n 要去的 root node
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # 有同一個 root node 代表準備要 loop 了
            if p1 == p2:
                return False
            
            # 比誰比較大坨
            # 小坨的 root 改成大坨的 root
            # 幫大坨的 root 加權重 (讓他變更大坨)
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]