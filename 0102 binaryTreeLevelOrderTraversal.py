"""
给你一个二叉树，请你返回其按层序遍历得到的节点值。（即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、广度优先搜索
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        nodes, result = deque(), []
        nodes.append(root)
        while nodes:
            vals = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(vals)
        return result


if __name__ == '__main__':
    s = Solution()
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20)
    node9 = TreeNode(9)
    node3 = TreeNode(3)
    node20.left, node20.right = node15, node7
    node3.left, node3.right = node9, node20
    r = s.levelOrder(node3)
    print(r)
