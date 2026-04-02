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
     * @return {number[]}
     */
    rightSideView(root) {
        let res = [];
        if (!root) return res;
        
        let queue = [root];

        while (queue.length !== 0) {
            let qlength = queue.length;
            let node;
            for (let i = 0; i < qlength; i++) {
                node = queue.shift();
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            res.push(node.val);
        }

        return res;
    }
}
