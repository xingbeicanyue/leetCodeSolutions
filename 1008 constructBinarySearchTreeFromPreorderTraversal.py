"""
返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，
对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。
此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）

题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

示例：
输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]
     8
   ┌─┴─┐
   5   10
 ┌─┴─┐ └─┐
 1   7   12

提示：
* 1 <= preorder.length <= 100
* 1 <= preorder[i] <= 10^8
* preorder 中的值互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        result = TreeNode(preorder[0])
        nodes = []  # 节点栈
        curNode = result
        for i in range(1, len(preorder)):
            val = preorder[i]
            while True:
                if val <= curNode.val:  # 向左
                    if curNode.left:
                        nodes.append(curNode)
                        curNode = curNode.left
                    else:
                        curNode.left = TreeNode(val)
                        break
                elif not nodes or val <= nodes[-1].val:  # 向右
                    if curNode.right:
                        # 不需要加入nodes，因为curNode左右子节点都已访问，不会再访问到
                        curNode = curNode.right
                    else:
                        curNode.right = TreeNode(val)
                        break
                else:  # 向上
                    curNode = nodes.pop()
        return result


def printTree(node: TreeNode):
    """ 按前序遍历的顺序输出节点值 """
    print(node.val if node else None, end=', ')
    if node is not None:
        printTree(node.left)
        printTree(node.right)


if __name__ == '__main__':
    s = Solution()
    r = s.bstFromPreorder([8, 5, 1, 7, 10, 12])
    printTree(r)
