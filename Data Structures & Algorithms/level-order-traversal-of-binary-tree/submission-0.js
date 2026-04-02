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
     * @return {number[][]}
     */
    levelOrder(root) {
        let res = [];
        if (root === null) return res;
        let queue = [root];

        while (queue.length !== 0) {
            let qlength = queue.length;
            let row = [];
            for (let i = 0; i < qlength; i++) {
                let node = queue.shift();
                row.push(node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            res.push(row);
        }

        return res;
    }
}
