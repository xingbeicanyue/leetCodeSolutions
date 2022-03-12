"""
二叉树展开为链表

给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树先序遍历顺序相同。

示例 1：
       1
     ┌─┴─┐
     2   5
   ┌─┴─┐ └─┐
   3   4   6
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
 
提示：
* 树中结点数在范围 [0, 2000] 内
* -100 <= Node.val <= 100

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:

        def doFlatten(node: TreeNode) -> TreeNode:
            """ 展开以node为根节点的树，返回链表尾 """
            if node.left:
                leftTail = doFlatten(node.left)
                node.left, node.right, leftTail.right, node = None, node.left, node.right, leftTail
            if node.right is None:
                return node
            return doFlatten(node.right)

        if root is not None:
            doFlatten(root)


def printTreeList(node: TreeNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.right
    print()


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    s.flatten(node1)
    printTreeList(node1)

    node1 = None
    s.flatten(node1)
    printTreeList(node1)

    node1 = TreeNode(0)
    s.flatten(node1)
    printTreeList(node1)
