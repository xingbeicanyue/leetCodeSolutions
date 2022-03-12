"""
旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head

        nodeCount, tailNode = 1, head  # 节点数 | 尾节点
        while tailNode.next is not None:
            nodeCount += 1
            tailNode = tailNode.next
        if k % nodeCount == 0:
            return head

        splitNode = head  # 分断节点（splitNode与splitNode.next断开）
        for i in range(nodeCount - k % nodeCount - 1):
            splitNode = splitNode.next
        result, splitNode.next, tailNode.next = splitNode.next, None, head
        return result


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    r = s.rotateRight(head, 2)
    printList(r)

    head = curNode = ListNode(0)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    r = s.rotateRight(head, 4)
    printList(r)
