class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Need review :(
        # create empty adj list -> (src : [])
        adj = { src:[] for src, dst in tickets }
        
        # create adj list -> (src : [dst list])
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            # base case
            if len(res) == len(tickets) + 1:
                return True
            # 如果現在的這個 node 沒有可以去的下一個地方就 return False
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                # backtracking here
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            
            # return False if no valid path
            return False
        
        dfs("JFK")
        return res
