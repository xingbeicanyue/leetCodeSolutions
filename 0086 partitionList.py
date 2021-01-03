"""
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例：
输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表、双指针
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        leftSNode = leftENode = ListNode(0)  # <x的链表头 | <x的链表尾
        rightSNode = rightENode = ListNode(0)  # >=x的链表头 | >=x的链表尾
        while head:
            if head.val < x:
                leftENode.next = leftENode = head
            else:
                rightENode.next = rightENode = head
            head = head.next
        leftENode.next, rightENode.next = rightSNode.next, None
        return leftSNode.next


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next


if __name__ == '__main__':
    s = Solution()
    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(5)
    curNode.next = curNode = ListNode(2)
    r = s.partition(head, 3)
    printList(r)
