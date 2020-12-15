"""
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
计算监控树的所有节点所需的最小摄像头数量。

示例 1：
     *
   ┌─┘
   C
 ┌─┴─┐
 *   *
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。

示例 2：
       *
     ┌─┘
     C
   ┌─┘
   *
 ┌─┘
 C
 └─┐
   *
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：
* 给定树的节点数的范围是 [1, 1000]。
* 每个节点的值都是 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-cameras
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、深度优先搜索、动态规划
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        def traversal(node) -> int:
            """ 迭代后序遍历
            :returns: 0:没有被监控到; 1:被其他摄像头监控到; 2:自己安装了摄像头
            """
            # 叶子节点不安装摄像头，其余节点后序遍历，非装不可时则安装摄像头
            if node is None:
                return 1
            lStatus = traversal(node.left)
            rStatus = traversal(node.right)
            if (lStatus and rStatus) == 0:  # 存在子节点没有被监控到
                nonlocal result
                result += 1
                return 2
            return 0 if lStatus == 1 and rStatus == 1 else 1

        if root is None:
            return 0
        result = 0
        rootStatus = traversal(root)
        return result + (rootStatus == 0)


if __name__ == '__main__':
    s = Solution()

    nodes = [TreeNode(0) for _ in range(5)]
    nodes[0].left, nodes[0].right = None, nodes[1]
    nodes[1].left, nodes[1].right = None, nodes[2]
    nodes[2].left, nodes[2].right = None, nodes[3]
    r = s.minCameraCover(nodes[0])
    print(r)

    nodes = [TreeNode(0) for _ in range(5)]
    nodes[0].left, nodes[0].right = nodes[1], None
    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = None, None
    nodes[3].left, nodes[3].right = None, None
    r = s.minCameraCover(nodes[0])
    print(r)

    nodes[0].left, nodes[0].right = nodes[1], None
    nodes[1].left, nodes[1].right = nodes[2], None
    nodes[2].left, nodes[2].right = nodes[3], None
    nodes[3].left, nodes[3].right = None, nodes[4]
    nodes[4].left, nodes[4].right = None, None
    r = s.minCameraCover(nodes[0])
    print(r)
