"""
删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
* 链表中结点的数目为 sz
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表、双指针
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = ListNode(0, head)
        left = right = head
        for i in range(n):
            right = right.next
        while right.next:
            left, right = left.next, right.next
        left.next = left.next.next
        return head.next


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
    r = s.removeNthFromEnd(head, 2)
    printList(r)

    head = ListNode(1)
    r = s.removeNthFromEnd(head, 1)
    printList(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    r = s.removeNthFromEnd(head, 1)
    printList(r)
