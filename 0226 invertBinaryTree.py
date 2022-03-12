"""
翻转二叉树

翻转一棵二叉树。

示例：
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

备注:
这个问题是受到 Max Howell 的原问题启发的：
谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


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

    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    r = s.invertTree(node1)
    printBinTree(r)
