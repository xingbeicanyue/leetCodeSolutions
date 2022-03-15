"""
恢复二叉搜索树

给你二叉搜索树的根节点 root ，该树中的恰好两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树。

示例 1：
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：
* 树上节点的数目在范围 [2, 1000] 内
* -2^31 <= Node.val <= 2^31 - 1

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional
from dataStructure import TreeNode, printTree


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        # 中序遍历 -> nodes
        nodes = []
        inorder(root)
        # 找到顺序错误的地方，并交换值
        errorIdx = -1
        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val:
                if errorIdx < 0:
                    errorIdx = i
                else:  # 找到第二个错误，交换
                    nodes[errorIdx].val, nodes[i + 1].val = nodes[i + 1].val, nodes[errorIdx].val
                    break
        else:  # 只有一个错误，交换该错误的2个节点值
            nodes[errorIdx].val, nodes[errorIdx + 1].val = nodes[errorIdx + 1].val, nodes[errorIdx].val


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    root.left = node2
    node2.right = node3
    s.recoverTree(root)
    printTree(root)

    root = TreeNode(3)
    node2 = TreeNode(1)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    root.left, root.right = node2, node3
    node3.left = node4
    s.recoverTree(root)
    printTree(root)
