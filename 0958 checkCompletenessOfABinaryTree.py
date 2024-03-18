"""
二叉树的完全性检验

给你一棵二叉树的根节点 root ，请你判断这棵树是否是一棵 完全二叉树 。
在一棵 完全二叉树 中，除了最后一层外，所有层都被完全填满，并且最后一层中的所有节点都尽可能靠左。
最后一层（第 h 层）中可以包含 1 到 2h 个节点。

示例 1：
输入：root = [1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，节点值为 {1} 和 {2,3} 的两层），且最后一层中的所有节点（{4,5,6}）尽可能靠左。

示例 2：
输入：root = [1,2,3,4,5,null,7]
输出：false
解释：值为 7 的节点不满足条件「节点尽可能靠左」。

提示：
树中节点数目在范围 [1, 100] 内
1 <= Node.val <= 1000

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 思路：层序遍历时检验是否都有子节点或子节点是否都靠左，最后一层应没有子节点，单独检验
        nodes = [root]
        while True:
            nextNodes = []
            shouldHaveChild = True
            for node in nodes:
                if shouldHaveChild:
                    if not node.right:
                        shouldHaveChild = False
                        if node.left:
                            nextNodes.append(node.left)
                    elif not node.left:
                        return False
                    else:
                        nextNodes.extend([node.left, node.right])
                elif node.left or node.right:
                    return False
            if not shouldHaveChild:  # 检验最后一排是否没有子节点
                for node in nextNodes:
                    if node.left or node.right:
                        return False
                return True
            nodes = nextNodes


if __name__ == "__main__":
    s = Solution()

    nodes = [TreeNode() for i in range(6)]
    nodes[0].left, nodes[0].right = nodes[1], nodes[2]
    nodes[1].left, nodes[1].right = nodes[3], nodes[4]
    nodes[2].left = nodes[5]
    r = s.isCompleteTree(nodes[0])
    print(r)

    nodes = [TreeNode() for i in range(6)]
    nodes[0].left, nodes[0].right = nodes[1], nodes[2]
    nodes[1].left, nodes[1].right = nodes[3], nodes[4]
    nodes[2].right = nodes[5]
    r = s.isCompleteTree(nodes[0])
    print(r)
