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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        if (!root) return !subRoot;
        return this.isSameTree(root, subRoot)
            || this.isSubtree(root.left, subRoot)
            || this.isSubtree(root.right, subRoot);
    }

    isSameTree(p, q) {
        if (!p) return !q;
        if (!q) return !p;

        return p.val === q.val
            && this.isSameTree(p.left, q.left)
            && this.isSameTree(p.right, q.right);
    }

}
