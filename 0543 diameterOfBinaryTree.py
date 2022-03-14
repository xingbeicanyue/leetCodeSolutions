"""
二叉树的直径

给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树
          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Tuple
from dataStructure import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def maxLength(node: TreeNode) -> Tuple[int, int]:
            """ 返回node左子树高度，最长路径长度 """
            leftSMaxLen = leftDMaxLen = rightSMaxLen = rightDMaxLen = 0
            if node.left:
                leftSMaxLen, leftDMaxLen = maxLength(node.left)
            if node.right:
                rightSMaxLen, rightDMaxLen = maxLength(node.right)
            return max(leftSMaxLen, rightSMaxLen) + 1, max(leftSMaxLen + rightSMaxLen + 1, leftDMaxLen, rightDMaxLen)

        # 思路与#124相同
        return maxLength(root)[1] - 1 if root else 0


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    r = s.diameterOfBinaryTree(root)
    print(r)
