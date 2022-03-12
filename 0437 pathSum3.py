"""
路径总和 III

给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
返回 3。和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(node: TreeNode, preSum: int) -> int:
            if node is None:
                return 0
            preSum += node.val
            result = preSums[preSum - sum]
            preSums[preSum] += 1
            result += dfs(node.left, preSum) + dfs(node.right, preSum)
            preSums[preSum] -= 1
            return result

        preSums = defaultdict(int)
        preSums[0] += 1
        return dfs(root, 0)


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(-3)
    node4 = TreeNode(3)
    node5 = TreeNode(2)
    node6 = TreeNode(11)
    node7 = TreeNode(3)
    node8 = TreeNode(-2)
    node9 = TreeNode(1)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    node4.left, node4.right = node7, node8
    node5.right = node9
    r = s.pathSum(node1, 8)
    print(r)
