class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        left, right = 0, len(matrix)-1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                # save topLeft
                topLeft = matrix[top][left+i]
                
                # move bottomLeft into topLeft
                matrix[top][left+i] = matrix[bottom-i][left]

                # move bottomRight into bottomLeft
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # move topRight into bottomRight
                matrix[bottom][right-i] = matrix[top+i][right]

                # move topLeft into topRight
                matrix[top+i][right] = topLeft
            
            left += 1
            right -= 1
