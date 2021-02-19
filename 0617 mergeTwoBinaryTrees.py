"""
合并二叉树

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。
合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        val1, left1, right1 = (root1.val, root1.left, root1.right) if root1 else (0, None, None)
        val2, left2, right2 = (root2.val, root2.left, root2.right) if root2 else (0, None, None)
        return TreeNode(val1 + val2, self.mergeTrees(left1, left2), self.mergeTrees(right1, right2))


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

    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(5)
    node1.left, node1.right = node2, node3
    node2.left = node4
    node5 = TreeNode(2)
    node6 = TreeNode(1)
    node7 = TreeNode(3)
    node8 = TreeNode(4)
    node9 = TreeNode(7)
    node5.left, node5.right = node6, node7
    node6.right = node8
    node7.right = node9
    r = s.mergeTrees(node1, node5)
    printBinTree(r)
