"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
调用 next() 将返回二叉搜索树中的下一个最小的数。

示例：
   7
 ┌─┴─┐
 3   15
   ┌─┴─┐
   9   20
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 
提示：
* next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
* 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、树、设计
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        # 方法同中序遍历
        self._nodeStack = []
        self._traversalLeft(root)

    def next(self) -> int:
        curNode = self._nodeStack.pop()
        self._traversalLeft(curNode.right)  # 提前遍历到下一个值
        return curNode.val

    def hasNext(self) -> bool:
        return len(self._nodeStack) > 0

    def _traversalLeft(self, node: TreeNode):
        """ 将node遍历至最左节点 """
        while node:
            self._nodeStack.append(node)
            node = node.left


if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15, node9, node20)
    node7 = TreeNode(7, node3, node15)
    it = BSTIterator(node7)
    print(it.next())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
