"""
二叉树的最大深度

给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from dataStructure import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        result, nodes = 0, [root]
        while len(nodes) > 0:
            nextNodes = []
            for node in nodes:
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)
            nodes = nextNodes
            result += 1
        return result


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(17)
    root.left, root.right = node2, node3
    node3.left, node3.right = node4, node5
    r = s.maxDepth(root)
    print(r)
