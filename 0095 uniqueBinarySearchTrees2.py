"""
不同的二叉搜索树 II

给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例：
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

提示：
* 0 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def createTree(n: int, minVal: int) -> List[TreeNode]:
            """ 创建n个节点的所有树
            :param n: 节点数
            :param minVal: 最小节点值
            """
            if n == 0:
                return [None]
            if n == 1:
                return [TreeNode(minVal)]
            result = []
            for i in range(n):
                leftTrees = createTree(i, minVal)
                rightTrees = createTree(n - 1 - i, minVal + i + 1)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        # 此处多棵树共用节点，如果不能共用则需克隆leftTree、rightTree整棵树
                        result.append(TreeNode(minVal + i, leftTree, rightTree))
            return result

        if n == 0:
            return []
        return createTree(n, 1)


if __name__ == '__main__':
    s = Solution()
    r = s.generateTrees(3)
    print(len(r))
