"""
给你二叉树的根节点 root ，返回它节点值的前序遍历。

示例 1：
 1
 └─┐
   2
 ┌─┘
 3
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
   1
 ┌─┘
 2
输入：root = [1,2]
输出：[1,2]

示例 5：
 1
 └─┐
   2
输入：root = [1,null,2]
输出：[1,2]

提示：
* 树中节点数目在范围 [0, 100] 内
* -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、树
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result, nodes, curNode = [], [], root
        while True:
            if curNode is None:
                if nodes:
                    curNode = nodes.pop()
                else:
                    break
            result.append(curNode.val)
            if curNode.right:
                nodes.append(curNode.right)
            curNode = curNode.left
        return result


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(1, 4)]

    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = nodes[2], None
    nodes[2].left, nodes[2].right = None, None
    r = s.preorderTraversal(nodes[0])
    print(r)

    r = s.preorderTraversal(None)
    print(r)

    nodes[0].left, nodes[0].right = None, None
    r = s.preorderTraversal(nodes[0])
    print(r)

    nodes[0].left, nodes[0].right = nodes[1], None
    nodes[1].left, nodes[1].right = None, None
    r = s.preorderTraversal(nodes[0])
    print(r)

    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = None, None
    r = s.preorderTraversal(nodes[0])
    print(r)
