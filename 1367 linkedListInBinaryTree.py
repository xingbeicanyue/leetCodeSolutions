"""
二叉树中的列表

给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。
如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，
那么请你返回 True ，否则返回 False 。
一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

示例 1：
        1
     /    \
    4      4*
     \    /
      2  2*
     /  /\
    1  6  8*
         /\
        1  3
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中带星号的节点构成了与链表对应的子路径。

示例 2：
        1*
     /    \
    4      4*
     \    /
      2  2*
     /  /\
    1  6* 8
         /\
        1  3
输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true

示例 3：
输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。

提示：
* 二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
* 链表包含的节点数目在 1 到 100 之间。
* 二叉树包含的节点数目在 1 到 2500 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # 方法1：
        # 深度优先遍历时进行匹配，并在匹配中使用KMP的nexts数组

        # 将链表转为字符列表
        chars, curListNode = [], head
        while curListNode:
            chars.append(curListNode.val)
            curListNode = curListNode.next

        # 计算nexts
        length = len(chars)
        nexts = [0] * length
        nexts[0] = -1
        i, matchLen = 1, 0
        while i < length - 1:
            if matchLen < 0 or chars[i] == chars[matchLen]:
                i += 1
                matchLen += 1
                nexts[i] = matchLen
            else:
                matchLen = nexts[matchLen]

        # 深度优先遍历
        def dfs(treeNode: TreeNode, charIdx: int) -> bool:
            if treeNode is None:
                return False
            if treeNode.val == chars[charIdx]:
                if charIdx + 1 == length:
                    return True
                return dfs(treeNode.left, charIdx + 1) or dfs(treeNode.right, charIdx + 1)
            if charIdx == 0:
                return dfs(treeNode.left, 0) or dfs(treeNode.right, 0)
            return dfs(treeNode, nexts[charIdx])
        return dfs(root, 0)


        # 方法2：
        # 深度优先遍历，以每个树节点为起始节点，逐次与链表节点比较

        # def match(curListNode: ListNode, curTreeNode: TreeNode) -> bool:
        #     if curListNode is None:  # 匹配完成
        #         return True
        #     if curTreeNode is None or curListNode.val != curTreeNode.val:  # 匹配失败
        #         return False
        #     # 当前可以匹配，继续匹配下个链表节点
        #     return match(curListNode.next, curTreeNode.left) or match(curListNode.next, curTreeNode.right)
        #
        # if root is None:
        #     return False
        # return match(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


if __name__ == '__main__':
    s = Solution()

    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(4)
    treeNode3 = TreeNode(4)
    treeNode4 = TreeNode(2)
    treeNode5 = TreeNode(2)
    treeNode6 = TreeNode(1)
    treeNode7 = TreeNode(6)
    treeNode8 = TreeNode(8)
    treeNode9 = TreeNode(1)
    treeNode10 = TreeNode(3)
    treeNode1.left, treeNode1.right = treeNode2, treeNode3
    treeNode2.right = treeNode4
    treeNode3.left = treeNode5
    treeNode4.left = treeNode6
    treeNode5.left, treeNode5.right = treeNode7, treeNode8
    treeNode8.left, treeNode8.right = treeNode9, treeNode10
    head = curListNode = ListNode(4)
    curListNode.next = curListNode = ListNode(2)
    curListNode.next = curListNode = ListNode(8)
    r = s.isSubPath(head, treeNode1)
    print(r)

    head = curListNode = ListNode(1)
    curListNode.next = curListNode = ListNode(4)
    curListNode.next = curListNode = ListNode(2)
    curListNode.next = curListNode = ListNode(6)
    r = s.isSubPath(head, treeNode1)
    print(r)

    head = curListNode = ListNode(1)
    curListNode.next = curListNode = ListNode(4)
    curListNode.next = curListNode = ListNode(2)
    curListNode.next = curListNode = ListNode(6)
    curListNode.next = curListNode = ListNode(8)
    r = s.isSubPath(head, treeNode1)
    print(r)
