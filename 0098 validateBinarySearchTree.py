"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
* 节点的左子树只包含小于当前节点的数。
* 节点的右子树只包含大于当前节点的数。
* 所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、深度优先搜索、递归
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def doValid(node: TreeNode, minVal, maxVal) -> bool:
            """ 验证node及其子节点大小关系、子节点是否∈(minVal, maxVal) """
            if node.left:
                if node.left.val >= node.val or (minVal is not None and node.left.val <= minVal) or \
                        not doValid(node.left, minVal, node.val):
                    return False
            if node.right:
                if node.right.val <= node.val or (maxVal is not None and node.right.val >= maxVal) or \
                        not doValid(node.right, node.val, maxVal):
                    return False
            return True

        return doValid(root, None, None) if root else True


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(1, 7)]

    nodes[1].left, nodes[1].right = nodes[0], nodes[2]
    nodes[0].left, nodes[0].right = None, None
    nodes[2].left, nodes[2].right = None, None
    r = s.isValidBST(nodes[1])
    print(r)

    nodes[4].left, nodes[4].right = nodes[0], nodes[3]
    nodes[0].left, nodes[0].right = None, None
    nodes[3].left, nodes[3].right = nodes[2], nodes[5]
    nodes[2].left, nodes[2].right = None, None
    nodes[5].left, nodes[5].right = None, None
    r = s.isValidBST(nodes[4])
    print(r)
