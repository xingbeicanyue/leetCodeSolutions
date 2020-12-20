"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
输入：
   1
    \
     3
    /
   2
输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

提示：
* 树中至少有 2 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树
重复题目：#783
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def inorderTraversal(node):
            """ 中序遍历 """
            if node is None:
                return
            inorderTraversal(node.left)
            nums.append(node.val)
            inorderTraversal(node.right)

        nums = []
        inorderTraversal(root)
        return min(nums[i] - nums[i - 1] for i in range(1, len(nums)))


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(4)]

    nodes[1].left, nodes[1].right = None, nodes[3]
    nodes[3].left, nodes[3].right = nodes[2], None
    nodes[2].left, nodes[2].right = None, None
    r = s.getMinimumDifference(nodes[1])
    print(r)
