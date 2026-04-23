class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建立一個課程的依賴關係表 -> a需要修過b,c才可以上 -> a: [b, c]
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)

        # 目前我們 dfs 的 path 有甚麼
        visitSet = set()

        def dfs(crs):
            # 重複遇到相同 crs -> 代表 loop 了 -> False
            if crs in visitSet:
                return False
            
            # 沒有需要修完才可以修這門課的限制 -> True
            if preMap[crs] == []:
                return True
            
            # 還有依賴的課程 -> 要準備遍歷那些課程
            # 把目前的課程加入 path
            visitSet.add(crs)

            # 有遇到沒辦法修的就 return False
            # 迴圈跑完沒有遇到 False 代表這門課可以修 -> True
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            # 遍歷完畢要把目前從 path 移除
            visitSet.remove(crs)

            # 因為這個課程是可以修的 -> 把他的依賴課程全部抹掉可以減少運算時間
            # 等於我們直接把它看作是一門可以修的課 (因為我們已經證實過了所以可以這樣做)
            preMap[crs] = []
            return True

        # 要從每個節點都跑一次
        # 因為怕有 seperate class, 例如: 1 -> 2, 3 -> 4
        # 有一個錯就 False, 沒有 False 離開迴圈可以 return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True        