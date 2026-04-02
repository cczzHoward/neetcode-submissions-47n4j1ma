class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 遍歷 nums 創造一個 dict, {number: count}
        number_dict = {}
        for num in nums:
            number_dict[num] = 1 + number_dict.get(num, 0)

        # 透過 sorted() 使用 number.dict.get(也就是value) 唯依據排序 number_dict
        # sorted() 的 output 會是一個 array
        sorted_numbers = sorted(number_dict, key=number_dict.get, reverse=True)
        return sorted_numbers[:k] 
        
