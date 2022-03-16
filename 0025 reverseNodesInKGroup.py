"""
K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：
* 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
* 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

示例 3：
输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

示例 4：
输入：head = [1], k = 1
输出：[1]

提示：
* 列表中节点的数量在范围 sz 内
* 1 <= sz <= 5000
* 0 <= Node.val <= 1000
* 1 <= k <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import Optional
from dataStructure import ListNode, printList


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        newHead = ListNode(0, head)
        lastRoundNode, lastNode = newHead, head  # 上一轮的结束节点 | 上一个节点
        while lastNode is not None:
            # 检查是否剩余>=k个节点
            tmpNode = lastNode
            for i in range(k):
                if tmpNode is None:
                    break
                tmpNode = tmpNode.next
            else:
                # 执行翻转
                curNode = lastNode.next  # 当前（要改变next指针的）节点
                for i in range(k - 1):
                    curNode.next, lastNode, curNode = lastNode, curNode, curNode.next
                lastRoundNode.next, lastRoundNode = lastNode, lastRoundNode.next
                lastRoundNode.next = lastNode = curNode
                continue
            break
        return newHead.next


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    r = s.reverseKGroup(head, 2)
    printList(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    r = s.reverseKGroup(head, 3)
    printList(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    r = s.reverseKGroup(head, 1)
    printList(r)

    head = ListNode(1)
    r = s.reverseKGroup(head, 1)
    printList(r)
