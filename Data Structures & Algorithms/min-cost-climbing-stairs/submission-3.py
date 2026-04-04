class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1, 2, 3, 0]
        #     ^ loop start from here
        # [3, 2, 3, 0]
        #     min(2+3, 2+0) => 2
        #  min(1+2, 1+3) = > 3
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])