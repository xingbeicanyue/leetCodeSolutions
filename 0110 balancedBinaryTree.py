"""
平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true

提示：
* 树中的节点数在范围 [0, 5000] 内
* -10^4 <= Node.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Tuple
from dataStructure import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def checkHeight(node: TreeNode) -> Tuple[bool, int]:
            """ 返回node是否平衡，node子树高度 """
            if node is None:
                return True, 0
            balanced, leftHeight = checkHeight(node.left)
            if not balanced:
                return False, 0
            balanced, rightHeight = checkHeight(node.right)
            return balanced and abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

        result, height = checkHeight(root)
        return result


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    root.left, root.right = node2, node3
    node3.left, node3.right = node4, node5
    r = s.isBalanced(root)
    print(r)

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    node6 = TreeNode(4)
    node7 = TreeNode(4)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node4.left, node4.right = node6, node7
    r = s.isBalanced(root)
    print(r)
