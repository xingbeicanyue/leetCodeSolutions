"""
排序链表

给你链表的头结点 head ，请将其按升序排列并返回排序后的链表。

进阶：
* 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
* 链表中节点的数目在范围 [0, 5 * 10^4] 内
* -10^5 <= Node.val <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def mergeSort(sNode: ListNode, eNode: ListNode) -> Tuple[ListNode, ListNode]:
            """ 从sNode至eNode.prev进行归并排序，若eNode为None则排序至链表尾
            :returns: 返回排序后的首尾节点（闭区间）
            """
            if sNode.next is eNode:
                return sNode, sNode
            # 快慢指针划分范围
            slow = fast = sNode
            while fast is not eNode:
                slow, fast = slow.next, fast.next
                if fast is eNode:
                    break
                fast = fast.next
            # 递归调用归并排序
            leftHead, leftTail = mergeSort(sNode, slow)
            rightHead, rightTail = mergeSort(slow, eNode)
            leftTail.next, rightTail.next = None, None
            # 归并
            curHead = curTail = ListNode(0)
            while leftHead is not None or rightHead is not None:
                if leftHead is None or (rightHead is not None and rightHead.val < leftHead.val):
                    curTail.next = curTail = rightHead
                    rightHead = rightHead.next
                else:
                    curTail.next = curTail = leftHead
                    leftHead = leftHead.next
            return curHead.next, curTail

        # 使用自上而下的归并排序，此处会有θ(lgn)的递归调用栈空间
        return mergeSort(head, None)[0] if head else None


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(4)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(3)
    r = s.sortList(head)
    printList(r)

    head = curNode = ListNode(-1)
    curNode.next = curNode = ListNode(5)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(0)
    r = s.sortList(head)
    printList(r)
