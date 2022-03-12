"""
二叉树中的最大路径和

路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中至多出现一次。
该路径至少包含一个节点，且不一定经过根节点。
路径和是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其最大路径和。

示例 1：
    1
  ┌─┴─┐
  2   3
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
    -10
   ┌─┴─┐
   9   20
     ┌─┴─┐
     15  7
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
* 树中节点数目范围是 [1, 3 * 10^4]
* -1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def maxPath(node: TreeNode) -> Tuple[int, int]:
            """ 返回以node为根节点的树中，以node为起点的路径最大长度、所有路径的最大长度 """
            if node.left:
                leftSMaxVal, leftDMaxVal = maxPath(node.left)
            else:
                leftSMaxVal = leftDMaxVal = -1001
            if node.right:
                rightSMaxVal, rightDMaxVal = maxPath(node.right)
            else:
                rightSMaxVal = rightDMaxVal = -1001
            # 所有路径的最大长度 = max(经过node的路径最大长度, 左子节点路径最大长度, 右子节点路径最大长度)
            return node.val + max(leftSMaxVal, rightSMaxVal, 0),\
                   max(node.val + max(leftSMaxVal, 0) + max(rightSMaxVal, 0), leftDMaxVal, rightDMaxVal)

        return maxPath(root)[1]


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left, node1.right = node2, node3
    r = s.maxPathSum(node1)
    print(r)

    node1 = TreeNode(-10)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5
    r = s.maxPathSum(node1)
    print(r)
