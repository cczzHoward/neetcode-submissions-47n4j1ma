class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        # 先找到數字可能存在的 ROW
        # O (log ROWS)
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        # 確定有找到數字可能存在的 ROW
        # 可能 out bound
        if not (top <= bot):
            return False
            
        
        # 在此 ROW 裡面找是否有數字
        # O (log COLS)
        left, right = 0, COLS-1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False