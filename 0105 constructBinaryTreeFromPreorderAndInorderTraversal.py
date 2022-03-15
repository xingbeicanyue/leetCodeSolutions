"""
从前序与中序遍历序列构造二叉树

给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]

提示:
* 1 <= preorder.length <= 3000
* inorder.length == preorder.length
* -3000 <= preorder[i], inorder[i] <= 3000
* preorder 和 inorder 均无重复元素
* inorder 均出现在 preorder
* preorder 保证为二叉树的前序遍历序列
* inorder 保证为二叉树的中序遍历序列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List, Optional
from dataStructure import TreeNode, printTree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def createTree(inorderSIdx: int, inorderEIdx: int) -> Optional[TreeNode]:
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


if __name__ == '__main__':
    s = Solution()

    r = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    printTree(r)

    r = s.buildTree([-1], [-1])
    printTree(r)
