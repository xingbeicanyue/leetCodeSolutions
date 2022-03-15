"""
二叉树的前序遍历

给你二叉树的根节点 root ，返回它节点值的前序遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
* 树中节点数目在范围 [0, 100] 内
* -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from dataStructure import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result, nodes = [], [root]
        while nodes:
            curNode = nodes.pop()
            if curNode is None:
                continue
            result.append(curNode.val)
            nodes.append(curNode.right)
            nodes.append(curNode.left)
        return result


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.right = node2
    node2.left = node3
    r = s.preorderTraversal(root)
    print(r)

    root = None
    r = s.preorderTraversal(root)
    print(r)

    root = TreeNode(1)
    r = s.preorderTraversal(root)
    print(r)

    root = TreeNode(1)
    node2 = TreeNode(2)
    root.left = node2
    r = s.preorderTraversal(root)
    print(r)

    root = TreeNode(1)
    node2 = TreeNode(2)
    root.right = node2
    r = s.preorderTraversal(root)
    print(r)
