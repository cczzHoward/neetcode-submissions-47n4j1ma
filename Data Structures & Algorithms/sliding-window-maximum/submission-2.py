class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # index (monotonically decreasing queue)
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove q[0] if it's outbound
            if l > q[0]:
                q.popleft()

            # add res when we get enough length
            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res