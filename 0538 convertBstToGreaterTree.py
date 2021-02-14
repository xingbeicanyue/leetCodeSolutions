"""
把二叉搜索树转换为累加树

给出二叉搜索树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
* 节点的左子树仅包含键小于节点键的节点。
* 节点的右子树仅包含键大于节点键的节点。
* 左右子树也必须是二叉搜索树。

示例 1：
            4(30)
      ┌───────┴───────┐
    1(36)           6(21)
  ┌───┴───┐       ┌───┴───┐
0(36)    2(35)  5(26)    7(15)
          └─┐             └─┐
          3(33)            8(8)
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
输入：root = [0,null,1]
输出：[1,null,1]

示例 3：
输入：root = [1,0,2]
输出：[3,3,2]

示例 4：
输入：root = [3,2,4,1]
输出：[7,9,4,10]

提示：
* 树中的节点数介于 0 和 10^4 之间。
* 每个节点的值介于 -10^4 和 10^4 之间。
* 树中的所有值互不相同。
* 给定的树为二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、深度优先搜索、二叉搜索树、递归
重复题目：#1038
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def doAddRight(node: TreeNode, base: int) -> int:
            if node is None:
                return base
            node.val += doAddRight(node.right, base)
            return doAddRight(node.left, node.val)

        doAddRight(root, 0)
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
    node2 = TreeNode(1)
    node3 = TreeNode(6)
    node4 = TreeNode(0)
    node5 = TreeNode(2)
    node6 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(3)
    node9 = TreeNode(8)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node5.right = node8
    node7.right = node9
    r = s.convertBST(node1)
    printBinTree(r)

    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node1.right = node2
    r = s.convertBST(node1)
    printBinTree(r)

    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(2)
    node1.left, node1.right = node2, node3
    r = s.convertBST(node1)
    printBinTree(r)

    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(4)
    node4 = TreeNode(1)
    node1.left, node1.right = node2, node3
    node2.left = node4
    r = s.convertBST(node1)
    printBinTree(r)
