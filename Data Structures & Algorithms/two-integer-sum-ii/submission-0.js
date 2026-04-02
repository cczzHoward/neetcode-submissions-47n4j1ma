class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let left = 0;
        let right = numbers.length-1;

        while (left<right) {
            let currentSum = numbers[left] + numbers[right];

            if (currentSum > target) {
                right--;
            } else if (currentSum < target) {
                left++;
            } else {
                return [left+1, right+1];
            }
        }
    }
}
