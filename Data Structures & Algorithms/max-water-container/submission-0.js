class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxArea = 0;
        let left = 0;
        let right = heights.length-1;

        while (left<right) {
            let currentPool = Math.min(heights[left], heights[right]) * (right-left);
            maxArea = Math.max(currentPool, maxArea);

            if (heights[left] < heights[right]) {
                left++;
            }  else {
                right--;
            }
        }

        return maxArea;
    }
}
