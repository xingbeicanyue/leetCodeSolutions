"""
根据前序和后序遍历构造二叉树

给定两个整数数组，preorder 和 postorder ，
其中 preorder 是一个具有无重复值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
如果存在多个答案，您可以返回其中任何一个。

示例 1：
输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

示例 2:
输入: preorder = [1], postorder = [1]
输出: [1]

提示：
* 1 <= preorder.length <= 30
* 1 <= preorder[i] <= preorder.length
* preorder 中所有值都不同
* postorder.length == preorder.length
* 1 <= postorder[i] <= postorder.length
* postorder 中所有值都不同
* 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from dataStructure import TreeNode, printTree


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:

        def constructChild(node: TreeNode, preSIdx: int, postSIdx: int, postEIdx: int):
            """ 在postorder[postSIdx, postEIdx]范围内构建node的子节点 """
            if postSIdx > postEIdx:  # 没有子节点
                return
            leftChildPostIdx, nodePostIdx = postValueIdxDict[preorder[preSIdx]], postValueIdxDict[node.val]
            node.left = TreeNode(preorder[preSIdx])  # 若有单个子节点则左子节点和右子节点都为解，这里统一设为左子节点
            constructChild(node.left, preSIdx + 1, postSIdx, leftChildPostIdx - 1)
            if leftChildPostIdx < nodePostIdx - 1:  # 如果有右子节点
                node.right = TreeNode(postorder[nodePostIdx - 1])
                constructChild(node.right, preSIdx + leftChildPostIdx - postSIdx + 2,
                               leftChildPostIdx + 1, nodePostIdx - 2)

        postValueIdxDict = {val: i for i, val in enumerate(postorder)}
        root = TreeNode(preorder[0])
        constructChild(root, 1, 0, len(preorder) - 2)
        return root


if __name__ == '__main__':
    s = Solution()

    r = s.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    printTree(r)

    r = s.constructFromPrePost([1], [1])
    printTree(r)

    r = s.constructFromPrePost([2, 1, 3], [3, 1, 2])
    printTree(r)
