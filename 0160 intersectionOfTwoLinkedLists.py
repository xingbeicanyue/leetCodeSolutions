"""
相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
 A:        a1 --> a2 --\
                        c1 --> c2 --> c3
 B: b1 --> b2 --> b3 --/

题目数据保证整个链式结构中不存在环。
注意，函数返回结果后，链表必须保持其原始结构。

示例 1：
 A:       4 --> 1 --\
                     8 --> 4 --> 5
 B: 5 --> 0 --> 1 --/
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
 A: 0 --> 9 --> 1 --\
                     2 --> 4
 B:             3 --/
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
 A: 2 --> 6 --> 4
 B:       1 --> 5
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

提示：
* listA 中节点数目为 m
* listB 中节点数目为 n
* 1 <= m, n <= 3 * 10^4
* 1 <= Node.val <= 10^5
* 0 <= skipA <= m
* 0 <= skipB <= n
* 如果 listA 和 listB 没有交点，intersectVal 为 0
* 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]

进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from dataStructure import ListNode, printList


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 如果两条链表长度相同且有交点，则在遍历完前就会相遇；如果没有交点，则两者都为None时（遍历完一次）结束
        # 如果两条链表长度不同且有交点，则在遍历另一条链表时相遇；如果没有交点，则两者都为None时（遍历完两条链表）结束
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA


if __name__ == '__main__':
    s = Solution()

    head1 = curNode = ListNode(4)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(8)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    head2 = curNode = ListNode(5)
    curNode.next = curNode = ListNode(0)
    curNode.next = curNode = ListNode(1)
    curNode.next = head1.next.next
    r = s.getIntersectionNode(head1, head2)
    printList(r)

    head1 = curNode = ListNode(0)
    curNode.next = curNode = ListNode(9)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(4)
    head2 = ListNode(3)
    head2.next = head1.next.next.next
    r = s.getIntersectionNode(head1, head2)
    printList(r)

    head1 = curNode = ListNode(2)
    curNode.next = curNode = ListNode(6)
    curNode.next = curNode = ListNode(4)
    head2 = curNode = ListNode(1)
    curNode.next = curNode = ListNode(5)
    r = s.getIntersectionNode(head1, head2)
    printList(r)
