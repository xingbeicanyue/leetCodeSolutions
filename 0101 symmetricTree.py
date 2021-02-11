"""
对称二叉树

给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、深度优先搜索、广度优先搜索
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        checkNodes, idx = [(root.left, root.right)], 0
        while idx < len(checkNodes):
            left, right = checkNodes[idx]
            idx += 1
            if left and right:
                if left.val != right.val:
                    return False
                checkNodes.append((left.left, right.right))
                checkNodes.append((left.right, right.left))
            elif left or right:
                return False
        return True


if __name__ == '__main__':
    s = Solution()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    r = s.isSymmetric(node1)
    print(r)

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    node1.left, node1.right = node2, node3
    node2.right = node4
    node3.right = node5
    r = s.isSymmetric(node1)
    print(r)
