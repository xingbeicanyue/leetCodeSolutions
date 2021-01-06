"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：
* 链表中节点的数目在范围 [0, 100] 内
* 0 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmpHead = curNode = ListNode(0, head)
        while curNode.next and curNode.next.next:
            nextNode = curNode.next
            nextNode2 = nextNode.next
            curNode.next, nextNode.next, nextNode2.next, curNode = nextNode2, nextNode2.next, nextNode, nextNode
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
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    r = s.swapPairs(head)
    printList(r)

    r = s.swapPairs(None)
    printList(r)

    head = ListNode(1)
    r = s.swapPairs(head)
    printList(r)
