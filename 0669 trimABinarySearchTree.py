"""
修剪二叉搜索树

给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
修剪树不应该改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在唯一的答案。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

示例 1：
输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]

示例 2：
输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]

提示：
* 树中节点数在范围 [1, 10^4] 内
* 0 <= Node.val <= 10^4
* 树中每个节点的值都是唯一的
* 题目数据保证输入是一棵有效的二叉搜索树
* 0 <= low <= high <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional
from dataStructure import TreeNode, printTree


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(2)
    root.left, root.right = node2, node3
    r = s.trimBST(root, 1, 2)
    printTree(r)

    root = TreeNode(3)
    node2 = TreeNode(0)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node5 = TreeNode(1)
    root.left, root.right = node2, node3
    node2.right = node4
    node4.left = node5
    r = s.trimBST(root, 1, 3)
    printTree(r)
