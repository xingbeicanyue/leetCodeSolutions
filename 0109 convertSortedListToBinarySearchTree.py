"""
有序链表转换二叉搜索树

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：二叉树、链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 先依次转为树节点列表，再按照列表转二叉搜索树的方法连接左右子节点
        # 即以1/2处节点作为根节点，1/4、3/4处节点作为其左右子节点，如此循环至叶子节点

        if head is None:
            return None
        # 转为树节点列表
        treeNodes = []
        while head is not None:
            treeNodes.append(TreeNode(head.val))
            head = head.next
        # 按照下标连接节点
        ranges = [(0, (len(treeNodes) - 1) // 2, len(treeNodes) - 1)]  # [(树最左节点下标, 根节点下标, 树最右节点下标)]
        while len(ranges) > 0:
            left, mid, right = ranges.pop()
            if left < mid:
                leftChildIdx = (left + mid - 1) // 2
                treeNodes[mid].left = treeNodes[leftChildIdx]
                ranges.append((left, leftChildIdx, mid - 1))
            if mid < right:
                rightChildIdx = (mid + 1 + right) // 2
                treeNodes[mid].right = treeNodes[rightChildIdx]
                ranges.append((mid + 1, rightChildIdx, right))
        return treeNodes[(len(treeNodes) - 1) // 2]


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

    head = curNode = ListNode(-10)
    curNode.next = curNode = ListNode(-3)
    curNode.next = curNode = ListNode(0)
    curNode.next = curNode = ListNode(5)
    curNode.next = curNode = ListNode(9)
    r = s.sortedListToBST(head)
    printBinTree(r)
