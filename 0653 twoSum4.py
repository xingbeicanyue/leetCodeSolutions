"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
输出: True
 
案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 思路
        # 将二叉查找树中序遍历为有序列表，再使用#167的方法

        def inorderTraversal(node: TreeNode, result: list):
            """ 二叉查找树中序遍历 """
            if node is None:
                return
            inorderTraversal(node.left, result)
            result.append(node.val)
            inorderTraversal(node.right, result)

        numbers = []
        inorderTraversal(root, numbers)
        if len(numbers) < 2:
            return False
        import bisect
        leftIdx, rightIdx = 0, min(len(numbers) - 1, bisect.bisect_right(numbers, k - numbers[0]))
        while leftIdx < rightIdx:
            sum_ = numbers[leftIdx] + numbers[rightIdx]
            if sum_ < k:
                leftIdx += 1
            elif sum_ > k:
                rightIdx -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node2, node4)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node7)
    node5 = TreeNode(5, node3, node6)
    result = s.findTarget(node5, 9)
    print(result)
    result = s.findTarget(node5, 28)
    print(result)
