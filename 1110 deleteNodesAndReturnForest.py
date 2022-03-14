"""
删点成林

给出二叉树的根节点 root，树上每个节点都有一个不同的值。
如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
返回森林中的每棵树。你可以按任意顺序组织答案。

示例 1：
输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

示例 2：
输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]

提示：
* 树中的节点数最大为 1000。
* 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
* to_delete.length <= 1000
* to_delete 包含一些从 1 到 1000、各不相同的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from dataStructure import TreeNode, printTrees


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def tryDelete(node: TreeNode, isRoot: bool) -> bool:
            """ 尝试移除node，若node未被移除且是根节点则加入结果中 """
            if node is None:
                return True
            needDelete = node.val in delValues
            if not needDelete and isRoot:
                result.append(node)
            if tryDelete(node.left, needDelete):
                node.left = None
            if tryDelete(node.right, needDelete):
                node.right = None
            return needDelete

        result = []
        delValues = set(to_delete)
        tryDelete(root, True)
        return result


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    r = s.delNodes(root, [3, 5])
    printTrees(r)

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(4)
    node4 = TreeNode(3)
    root.left, root.right = node2, node3
    node2.right = node4
    r = s.delNodes(root, [3])
    printTrees(r)
