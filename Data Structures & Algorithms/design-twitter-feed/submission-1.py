class Twitter:
    # 不好意思這題真的報幹難欸?
    # 這邊先評價一個 hard :(

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # UserId -> list of [count, tweekIds]
        # 追蹤人的ID -> 被追蹤的ID set
        self.followMap = defaultdict(set) # UserId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 把新的 tweet 插入 tweetMap 裡面
        self.tweetMap[userId].append([self.count, tweetId])
        # 計數器 -1 (因為 python maxHeap 實作需求)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []

        # 把自己也加進去(把自己發 tweet 也考慮)
        self.followMap[userId].add(userId)
        # 遍歷自己有 follow 的人
        for followeeId in self.followMap[userId]:
            # 確認這個目前遍歷到的人有發 tweet
            if followeeId in self.tweetMap:
                # 取尾巴(最新)的文章 index
                index = len(self.tweetMap[followeeId]) - 1
                # 取得該文章的 pair value [count, tweekId]
                count, tweetId = self.tweetMap[followeeId][index]
                # 把資料丟進 minHeap (這邊 index-1 是提前計算, 指向下一個要去的文章 index)
                minHeap.append([count, tweetId, followeeId, index-1])
        
        # 轉換成 maxHeap (用 minHeap 且 value(count) 換成負數實作)
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            # 取出最新文章丟進 res 裡面
            # 這邊的 index 就是提前算好的所以不用算下一個 index 的位置
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # 如果還有文章的話要把文章丟回 minHeap 裡面
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                # index 處理與 line 29 相同
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        
        # 處理完畢 res 就會是最新的文章(最多 10 筆)
        return res
                
    def follow(self, followerId: int, followeeId: int) -> None:
        # 把 follow 記錄到 followMap
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 把 follow 從紀錄(followMap)中移除
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
