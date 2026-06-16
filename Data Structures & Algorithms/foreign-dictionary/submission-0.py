class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 這是 neetcode 150 裡面寫到的第 146 題
        # 他是這 146 題中我覺得最難的, 甚至看影片都沒有看很懂, 一定要複習的一題...

        adj = { c:set() for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # 沒有答案的 case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # 在這兩個單字中找字母大小關係並加進 adj dict
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False = visited, True = current path
        res = [] # 我們用 postOrder dfs 所以最後要 reverse 在回傳答案

        # 這題的 dfs 我看得很不懂 (好難..)
        def dfs(c):
            # 發現 loop (沒有完全懂)
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False

            # postOrder 應該是指這邊才 append (不確定)
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)