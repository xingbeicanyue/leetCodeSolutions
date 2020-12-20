"""
给定一个二叉树，返回它的后序遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result, nodes, curNode = [], [], root
        while True:
            if curNode is None:
                if nodes:
                    curNode = nodes.pop()
                else:
                    break
            result.append(curNode.val)
            if curNode.left:
                nodes.append(curNode.left)
            curNode = curNode.right
        # 如果不希望逆向操作，可以在遍历时就按后序的顺序加入，但需要额外的变量来区分是访问右子节点还是访问自己
        result.reverse()
        return result


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(1, 4)]
    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = nodes[2], None
    nodes[2].left, nodes[2].right = None, None
    r = s.postorderTraversal(nodes[0])
    print(r)
