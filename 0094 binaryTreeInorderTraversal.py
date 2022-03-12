"""
二叉树的中序遍历

给定一个二叉树的根节点 root ，返回它的中序遍历。

示例 1：
 1
 └─┐
   2
 ┌─┘
 3
输入：root = [1,null,2,3]
输出：[1,3,2]

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
输出：[2,1]

示例 5：
 1
 └─┐
   2
输入：root = [1,null,2]
输出：[1,2]
 
提示：
* 树中节点数目在范围 [0, 100] 内
* -100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 这里使用栈的中序遍历法，时间Θ(n)，空间Θ(n)
        # Morris遍历法可以在Θ(n)时间，Θ(1)空间内完成
        result, nodes, curNode = [], [], root
        toRight = False  # True表示第二次访问curNode，只看右子节点
        while True:
            if curNode:
                if toRight:
                    result.append(curNode.val)
                    curNode, toRight = curNode.right, False
                else:
                    nodes.append(curNode)
                    curNode = curNode.left
            else:
                if nodes:
                    curNode, toRight = nodes.pop(), True
                else:
                    break
        return result


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(1, 4)]

    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = nodes[2], None
    nodes[2].left, nodes[2].right = None, None
    r = s.inorderTraversal(nodes[0])
    print(r)

    r = s.inorderTraversal(None)
    print(r)

    nodes[0].left, nodes[0].right = None, None
    r = s.inorderTraversal(nodes[0])
    print(r)

    nodes[0].left, nodes[0].right = nodes[1], None
    nodes[1].left, nodes[1].right = None, None
    r = s.inorderTraversal(nodes[0])
    print(r)

    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = None, None
    r = s.inorderTraversal(nodes[0])
    print(r)
