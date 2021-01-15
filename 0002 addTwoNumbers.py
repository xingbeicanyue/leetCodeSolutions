"""
两数相加

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
  2 -> 4 -> 3
  5 -> 6 -> 4
  7 -> 0 -> 8
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
* 每个链表中的节点数在范围 [1, 100] 内
* 0 <= Node.val <= 9
* 题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表、数学
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = resultTail = ListNode(0)
        carryFlag = 0  # 进位符
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryFlag
            carryFlag = val // 10
            resultTail.next = resultTail = ListNode(val % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carryFlag:
            resultTail.next = ListNode(1)
        return result.next


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    l1 = curNode = ListNode(2)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(3)
    l2 = curNode = ListNode(5)
    curNode.next = curNode = ListNode(6)
    curNode.next = curNode = ListNode(4)
    r = s.addTwoNumbers(l1, l2)
    printList(r)

    l1 = ListNode(0)
    l2 = ListNode(0)
    r = s.addTwoNumbers(l1, l2)
    printList(r)

    l1 = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    l2 = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(9)
    r = s.addTwoNumbers(l1, l2)
    printList(r)
