class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 這題感覺也要多看幾次
        # 第一次看解法有點沒辦法完全理解
        # topological sort 之後要再看一下
        # ^ neetcode 影片中不要硬學這個 sort, 而是透過這題學習這個 sort
        preReq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        output = []
        # visit 放已處理過的 course -> 代表可以上的 course
        # cycle 放目前的 path -> 重複遇到代表 loop -> false
        visit, cycle = set(), set()
        def dfs(crs):
            # 是否 loop 了
            if crs in cycle:
                return False
            # 是否處理過了
            if crs in visit:
                return True

            # 開始處理這個 course, 加到目前 path 裡
            cycle.add(crs)
            # 遍歷每個 prerequisite
            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            # 遍歷完畢, 從目前 path 移除
            cycle.remove(crs)
            # 這個 course 沒問題, 可以上 -> 加到 output 以及 visit 
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output