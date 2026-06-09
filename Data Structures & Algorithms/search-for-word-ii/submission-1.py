# 這題也好難, code 多又用到很多 dsa
# Tries, Backtracking, dfs
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # 把不符合資格 case 先 return
            # outbound
            # 不是我們要找的字母
            # 已經遍歷過的字母
            if (r<0 or c<0 or
                r==ROWS or c==COLS or
                board[r][c] not in node.children or
                (r, c) in visit):
                return
            
            # 確認可以走這一格字母 (加入visit)
            visit.add((r, c))
            # 更新我們在的 node (往下一個字母更新)
            node = node.children[board[r][c]]
            # 更新目前拚出來的字
            word += board[r][c]
            # 如果這個 node 是單字結尾就把結果塞進 res
            if node.isWord:
                res.add(word)
            
            # 往四周的方向走走看
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            # backtracking 要記得把原本在 visit 裡面的 (r, c) 拿掉
            visit.remove((r, c))
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        # 記得要把 res 從 set 轉回 list
        return list(res)