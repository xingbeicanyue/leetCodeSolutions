"""
合并两个有序链表

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

提示：
* 两个链表的节点数目范围是 [0, 50]
* -100 <= Node.val <= 100
* l1 和 l2 均按非递减顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from dataStructure import ListNode, printList


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = resultTail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                resultTail.next = resultTail = l1
                l1 = l1.next
            else:
                resultTail.next = resultTail = l2
                l2 = l2.next
        resultTail.next = l1 if l1 else l2
        return result.next


if __name__ == '__main__':
    s = Solution()

    l1 = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(4)
    l2 = curNode = ListNode(1)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    r = s.mergeTwoLists(l1, l2)
    printList(r)

    l1 = l2 = None
    r = s.mergeTwoLists(l1, l2)
    printList(r)

    l1 = None
    l2 = ListNode(0)
    r = s.mergeTwoLists(l1, l2)
    printList(r)
