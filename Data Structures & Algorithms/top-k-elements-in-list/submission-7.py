class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1
        
        # nums -> [6, 6, 6, 9, 9, 10]
        # count_dict -> {6:3, 9:2, 10:1}
        
        sorted_count_dict = sorted(count_dict, key= lambda x: count_dict[x], reverse=True)

        return sorted_count_dict[:k]