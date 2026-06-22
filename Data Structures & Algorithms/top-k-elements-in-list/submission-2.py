class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        sorted_number = sorted(count, key=count.get, reverse=True)
        return sorted_number[:k]