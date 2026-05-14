class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 不能整除代表根本排不出來
        if len(hand) % groupSize:
            return False

        # 建立 mapping table : number -> count 
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # minHeap 來 maintain 目前還存在的最小卡牌
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            # 看 groupSize 是否找的到相符的卡牌
            for i in range(first, first+groupSize):
                # 如果 hand = [1, 2, 4]
                # 我們會嘗試找 1, 2, 3 -> 3 不存在所以 False
                if i not in count:
                    return False
                count[i] -= 1
                
                # 如果拿完後沒有 i 的這張卡排了
                # 從 heap 移除
                if count[i] == 0:
                    # 如果 minHeap 最小的數字不是我們要移除的數字
                    # 代表不可能可以 True -> False
                    if i != minHeap[0]:
                        return False
                    
                    # 正常移除卡牌
                    heapq.heappop(minHeap)
        
        return True


        