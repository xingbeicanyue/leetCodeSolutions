"""
二叉搜索树中第K小的元素

给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、二分查找
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 思路：中序遍历至第k个节点后终止遍历

        def traversal(node: TreeNode):
            if node is not None:
                res = traversal(node.left)
                if res is not None:
                    return res
                nonlocal k
                if k == 1:
                    return node.val
                k -= 1
                res = traversal(node.right)
                if res is not None:
                    return res
            return None

        return traversal(root)


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(7)]

    nodes[3].left, nodes[3].right = nodes[1], nodes[4]
    nodes[1].left, nodes[1].right = None, nodes[2]
    nodes[2].left, nodes[2].right = None, None
    nodes[4].left, nodes[4].right = None, None
    r = s.kthSmallest(nodes[3], 1)
    print(r)

    nodes[5].left, nodes[5].right = nodes[3], nodes[6]
    nodes[3].left, nodes[3].right = nodes[2], nodes[4]
    nodes[2].left, nodes[2].right = nodes[1], None
    nodes[1].left, nodes[1].right = None, None
    nodes[4].left, nodes[4].right = None, None
    nodes[6].left, nodes[6].right = None, None
    r = s.kthSmallest(nodes[5], 3)
    print(r)
