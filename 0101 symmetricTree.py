"""
对称二叉树

给你一个二叉树的根节点 root ，检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：
* 树中节点数目在范围 [1, 1000] 内
* -100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from dataStructure import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 以循环和层次遍历的方式比较两侧
        if root is None:
            return True
        checkNodes, idx = [(root.left, root.right)], 0
        while idx < len(checkNodes):
            left, right = checkNodes[idx]
            idx += 1
            if left and right:
                if left.val != right.val:
                    return False
                checkNodes.append((left.left, right.right))
                checkNodes.append((left.right, right.left))
            elif left or right:
                return False
        return True


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    r = s.isSymmetric(root)
    print(r)

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    root.left, root.right = node2, node3
    node2.right = node4
    node3.right = node5
    r = s.isSymmetric(root)
    print(r)
