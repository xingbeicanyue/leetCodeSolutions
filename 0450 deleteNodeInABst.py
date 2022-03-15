"""
删除二叉搜索树中的节点

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
* 首先找到需要删除的节点；
* 如果找到了，删除它。

示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7],
另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

示例 3:
输入: root = [], key = 0
输出: []

提示:
* 节点数的范围 [0, 10^4].
* -10^5 <= Node.val <= 10^5
* 节点值唯一
* root 是合法的二叉搜索树
* -10^5 <= key <= 10^5

进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional
from dataStructure import TreeNode, printTree


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findPrev(node: TreeNode) -> TreeNode:
            """ 寻找node前驱节点并断开其与父节点的连接 """
            parent, node = node, node.left
            while node.right is not None:
                parent, node = node, node.right
            parent.right = None
            return node

        if root is None:
            return None
        leftNode, rightNode = root.left, root.right
        if root.val == key:
            if leftNode is None:
                return rightNode
            elif rightNode is None:
                return leftNode
            else:  # 被删除的节点有两个子节点，用前驱节点代替
                if leftNode.right is None:
                    leftNode.right = rightNode
                    return leftNode
                else:
                    prevNode = result = findPrev(root)
                    prevNode.right = root.right
                    while prevNode.left:
                        prevNode = prevNode.left
                    prevNode.left = leftNode
                    return result
        elif root.val < key:
            root.right = self.deleteNode(rightNode, key)
        else:
            root.left = self.deleteNode(leftNode, key)
        return root


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    r = s.deleteNode(root, 3)
    printTree(r)

    root = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    r = s.deleteNode(root, 0)
    printTree(r)

    root = None
    r = s.deleteNode(root, 0)
    printTree(r)
