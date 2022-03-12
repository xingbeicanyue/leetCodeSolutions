"""
从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def createTree(inorderSIdx: int, inorderEIdx: int) -> TreeNode:
            """ 在inorder[inorderSIdx: inorderEIdx]范围内构建树 """
            if inorderSIdx >= inorderEIdx:
                return None
            nonlocal preorderSIdx
            inorderIdx = inorderIdxs[preorder[preorderSIdx]]
            preorderSIdx += 1
            return TreeNode(inorder[inorderIdx], createTree(inorderSIdx, inorderIdx),
                            createTree(inorderIdx + 1, inorderEIdx))

        preorderSIdx = 0
        inorderIdxs = {val: i for i, val in enumerate(inorder)}  # {节点值: 在中序遍历结果中的下标}
        return createTree(0, len(inorder))


def printBinTree(node: TreeNode):
    """ 按层次遍历顺序打印二叉树 """
    nodeQueue, nodeIdx, noneCount = [node], 0, 0
    while nodeIdx < len(nodeQueue):
        node = nodeQueue[nodeIdx]
        nodeIdx += 1
        if node is None:
            noneCount += 1
        else:
            if noneCount > 0:
                print('null,' * noneCount, end='')
                noneCount = 0
            print(str(node.val) + ',', end='')
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
    print()


if __name__ == '__main__':
    s = Solution()
    r = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    printBinTree(r)
