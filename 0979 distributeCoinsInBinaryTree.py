"""
在二叉树中分配硬币

给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。
(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。
返回使每个结点上只有一枚硬币所需的移动次数。

示例 1：
   3
 ┌─┴─┐
 0   0
输入：[3,0,0]
输出：2
解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。

示例 2：
   0
 ┌─┴─┐
 3   0
输入：[0,3,0]
输出：3
解释：从根结点的左子结点开始，我们将两枚硬币移到根结点上 [移动两次]。然后，我们把一枚硬币从根结点移到右子结点上。

示例 3：
   1
 ┌─┴─┐
 0   2
输入：[1,0,2]
输出：2

示例 4：
   1
 ┌─┴─┐
 0   0
 └┐
  3
输入：[1,0,0,null,3]
输出：4
 
提示：
* 1<= N <= 100
* 0 <= node.val <= N

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-coins-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、深度优先搜索
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        def traversal(node: TreeNode) -> int:
            """ 后序遍历
            :returns: 返回node给父节点的金币数，如果需要从父节点拿金币则为负数
            """
            if node is None:
                return 0
            diff = node.val + traversal(node.left) + traversal(node.right) - 1  # 金币流量，累计入最终结果
            nonlocal result
            result += abs(diff)
            return diff

        result = 0
        traversal(root)
        return result


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(0) for _ in range(4)]

    nodes[0].val, nodes[0].left, nodes[0].right = 3, nodes[1], nodes[2]
    nodes[1].val, nodes[1].left, nodes[1].right = 0, None, None
    nodes[2].val, nodes[2].left, nodes[2].right = 0, None, None
    r = s.distributeCoins(nodes[0])
    print(r)

    nodes = [TreeNode(0) for _ in range(4)]
    nodes[0].val, nodes[0].left, nodes[0].right = 0, nodes[1], nodes[2]
    nodes[1].val, nodes[1].left, nodes[1].right = 3, None, None
    nodes[2].val, nodes[2].left, nodes[2].right = 0, None, None
    r = s.distributeCoins(nodes[0])
    print(r)

    nodes = [TreeNode(0) for _ in range(4)]
    nodes[0].val, nodes[0].left, nodes[0].right = 1, nodes[1], nodes[2]
    nodes[1].val, nodes[1].left, nodes[1].right = 0, None, None
    nodes[2].val, nodes[2].left, nodes[2].right = 2, None, None
    r = s.distributeCoins(nodes[0])
    print(r)

    nodes = [TreeNode(0) for _ in range(4)]
    nodes[0].val, nodes[0].left, nodes[0].right = 1, nodes[1], nodes[2]
    nodes[1].val, nodes[1].left, nodes[1].right = 0, None, nodes[3]
    nodes[2].val, nodes[2].left, nodes[2].right = 0, None, None
    nodes[3].val, nodes[3].left, nodes[3].right = 3, None, None
    r = s.distributeCoins(nodes[0])
    print(r)
