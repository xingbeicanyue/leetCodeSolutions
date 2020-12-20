"""
给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。
其中，克隆树 cloned 是原始树 original 的一个副本 。
请找出在树 cloned 中，与 target 相同的节点，并返回对该节点的引用
（在 C/C++ 等有指针的语言中返回节点指针，其他语言返回节点本身）。

注意：
* 你不能对两棵二叉树，以及 target 节点进行更改。
* 只能返回对克隆树 cloned 中已有的节点的引用。

进阶：如果树中允许出现值相同的节点，你将如何解答？

示例 1:
   7           7
 ┌─┴─┐       ┌─┴─┐
 4  3(t)     4  3(r)
   ┌─┴─┐       ┌─┴─┐
   6  19       6  19
输入: tree = [7,4,3,null,null,6,19], target = 3
输出: 3
解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用(t)标记。
      答案是树 cloned 中的用(r)标记的节点（其他示例类似）。

示例 2:
  7(t)   7(r)
输入: tree = [7], target =  7
输出: 7

示例 3:
 8         8
 └┐        └┐
  6         6
  └┐        └┐
   5         5
   └┐        └┐
    4(t)      4(r)
    └┐        └┐
     3         3
     └┐        └┐
      2         2
      └┐        └┐
       1         1
输入: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
输出: 4

示例 4:
            1                      1
       ┌────┴────┐            ┌────┴────┐
       2         3            2         3
   ┌───┴──┐    ┌─┴─┐      ┌───┴──┐    ┌─┴─┐
   4     5(t)  6   7      4     5(r)  6   7
 ┌─┴─┐   ┌┘             ┌─┴─┐   ┌┘
 8   9  10              8   9  10
输入: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
输出: 5

示例 5:
    1      1
   ┌┘     ┌┘
 2(t)   2(r)
 ┌┘     ┌┘
 3      3
输入: tree = [1,2,null,3], target = 2
输出: 2

提示：
* 树中节点的数量范围为 [1, 10^4] 。
* 同一棵树中，没有值相同的节点。
* target 节点是树 original 中的一个节点，并且不会是 null 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        return (self.getTargetCopy(original.left, cloned.left, target) if original.left else None) or \
               (self.getTargetCopy(original.right, cloned.right, target) if original.right else None)


if __name__ == '__main__':
    s = Solution()
    nodes = [TreeNode(i) for i in range(20)]
    clonedNodes = [TreeNode(i) for i in range(20)]

    nodes[7].left, nodes[7].right = nodes[4], nodes[3]
    nodes[4].left, nodes[4].right = None, None
    nodes[3].left, nodes[3].right = nodes[6], nodes[19]
    nodes[6].left, nodes[6].right = None, None
    nodes[19].left, nodes[19].right = None, None
    clonedNodes[7].left, clonedNodes[7].right = clonedNodes[4], clonedNodes[3]
    clonedNodes[4].left, clonedNodes[4].right = None, None
    clonedNodes[3].left, clonedNodes[3].right = clonedNodes[6], clonedNodes[19]
    clonedNodes[6].left, clonedNodes[6].right = None, None
    clonedNodes[19].left, clonedNodes[19].right = None, None
    r = s.getTargetCopy(nodes[7], clonedNodes[7], nodes[3])
    print(r.val)

    nodes[7].left, nodes[7].right = None, None
    clonedNodes[7].left, clonedNodes[7].right = None, None
    r = s.getTargetCopy(nodes[7], clonedNodes[7], nodes[7])
    print(r.val)

    nodes[8].left, nodes[8].right = None, nodes[6]
    nodes[6].left, nodes[6].right = None, nodes[5]
    nodes[5].left, nodes[5].right = None, nodes[4]
    nodes[4].left, nodes[4].right = None, nodes[3]
    nodes[3].left, nodes[3].right = None, nodes[2]
    nodes[2].left, nodes[2].right = None, nodes[1]
    nodes[1].left, nodes[1].right = None, None
    clonedNodes[8].left, clonedNodes[8].right = None, clonedNodes[6]
    clonedNodes[6].left, clonedNodes[6].right = None, clonedNodes[5]
    clonedNodes[5].left, clonedNodes[5].right = None, clonedNodes[4]
    clonedNodes[4].left, clonedNodes[4].right = None, clonedNodes[3]
    clonedNodes[3].left, clonedNodes[3].right = None, clonedNodes[2]
    clonedNodes[2].left, clonedNodes[2].right = None, clonedNodes[1]
    clonedNodes[1].left, clonedNodes[1].right = None, None
    r = s.getTargetCopy(nodes[8], clonedNodes[8], nodes[4])
    print(r.val)

    nodes[1].left, nodes[1].right = nodes[2], nodes[3]
    nodes[2].left, nodes[2].right = nodes[4], nodes[5]
    nodes[3].left, nodes[3].right = nodes[6], nodes[7]
    nodes[4].left, nodes[4].right = nodes[8], nodes[9]
    nodes[5].left, nodes[5].right = nodes[10], None
    nodes[6].left, nodes[6].right = None, None
    nodes[7].left, nodes[7].right = None, None
    nodes[8].left, nodes[8].right = None, None
    nodes[9].left, nodes[9].right = None, None
    nodes[10].left, nodes[10].right = None, None
    clonedNodes[1].left, clonedNodes[1].right = clonedNodes[2], clonedNodes[3]
    clonedNodes[2].left, clonedNodes[2].right = clonedNodes[4], clonedNodes[5]
    clonedNodes[3].left, clonedNodes[3].right = clonedNodes[6], clonedNodes[7]
    clonedNodes[4].left, clonedNodes[4].right = clonedNodes[8], clonedNodes[9]
    clonedNodes[5].left, clonedNodes[5].right = clonedNodes[10], None
    clonedNodes[6].left, clonedNodes[6].right = None, None
    clonedNodes[7].left, clonedNodes[7].right = None, None
    clonedNodes[8].left, clonedNodes[8].right = None, None
    clonedNodes[9].left, clonedNodes[9].right = None, None
    clonedNodes[10].left, clonedNodes[10].right = None, None
    r = s.getTargetCopy(nodes[1], clonedNodes[1], nodes[5])
    print(r.val)

    nodes[1].left, nodes[1].right = nodes[2], None
    nodes[2].left, nodes[2].right = nodes[3], None
    nodes[3].left, nodes[3].right = None, None
    clonedNodes[1].left, clonedNodes[1].right = clonedNodes[2], None
    clonedNodes[2].left, clonedNodes[2].right = clonedNodes[3], None
    clonedNodes[3].left, clonedNodes[3].right = None, None
    r = s.getTargetCopy(nodes[1], clonedNodes[1], nodes[2])
    print(r.val)
