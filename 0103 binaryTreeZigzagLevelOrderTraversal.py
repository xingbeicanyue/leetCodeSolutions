"""
二叉树的锯齿形层序遍历

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：
[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        def layerTraversal():
            """ 逆序遍历nodes，子节点加入nextNodes """
            vals = []
            for node in reversed(nodes):
                vals.append(node.val)
                firstChild, secondChild = (node.left, node.right) if layer == 1 else (node.right, node.left)
                if firstChild:
                    nextNodes.append(firstChild)
                if secondChild:
                    nextNodes.append(secondChild)
            result.append(vals)

        layer = 1  # 1:奇数层; 0:偶数层 （从1开始）
        nodes, nextNodes, result = [root], [], []
        if root:
            while nodes:
                layerTraversal()
                nodes, nextNodes, layer = nextNodes, [], 1 - layer
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
    r = s.zigzagLevelOrder(node3)
    print(r)
