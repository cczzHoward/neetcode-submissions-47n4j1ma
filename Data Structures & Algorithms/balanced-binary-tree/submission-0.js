/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        let flag = true;
        let findDepth = (root) => {
            if (!root) return 0;
            
            const leftDepth = findDepth(root.left);
            const rightDepth = findDepth(root.right);

            if (Math.abs(leftDepth-rightDepth) > 1) flag = false;
            return Math.max(leftDepth, rightDepth) + 1;
        };
        findDepth(root)
        return flag
    }
}
