"""
移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-linked-list-elements/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmpHead = ListNode(0, head)
        prevNode, curNode = tmpHead, head
        while curNode:
            if curNode.val == val:
                prevNode.next = curNode.next
            else:
                prevNode = curNode
            curNode = curNode.next
        return tmpHead.next


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
    curNode.next = curNode = ListNode(6)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    curNode.next = curNode = ListNode(6)
    r = s.removeElements(head, 6)
    printList(r)
