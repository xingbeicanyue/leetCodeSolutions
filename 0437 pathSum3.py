"""
路径总和 III

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3

提示:
* 二叉树的节点个数的范围是 [0,1000]
* -10^9 <= Node.val <= 10^9
* -1000 <= targetSum <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from dataStructure import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(node: TreeNode, preSum: int) -> int:
            if node is None:
                return 0
            preSum += node.val
            result = preSums[preSum - sum]
            preSums[preSum] += 1
            result += dfs(node.left, preSum) + dfs(node.right, preSum)
            preSums[preSum] -= 1
            return result

        preSums = defaultdict(int)
        preSums[0] += 1
        return dfs(root, 0)


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(-3)
    node4 = TreeNode(3)
    node5 = TreeNode(2)
    node6 = TreeNode(11)
    node7 = TreeNode(3)
    node8 = TreeNode(-2)
    node9 = TreeNode(1)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.right = node6
    node4.left, node4.right = node7, node8
    node5.right = node9
    r = s.pathSum(root, 8)
    print(r)

    root = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(5)
    node10 = TreeNode(1)
    root.left, root.right = node2, node3
    node2.left = node4
    node3.left, node3.right = node5, node6
    node4.left, node4.right = node7, node8
    node6.left, node6.right = node9, node10
    r = s.pathSum(root, 22)
    print(r)
