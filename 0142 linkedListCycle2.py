"""
环形链表 II

给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：
* 你是否可以使用 O(1) 空间解决此题？
示例 1：
    3 --> 2 --> 0 --> -4
          ^            │
          └────────────┘
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    1 --> 2
    ^     │
    └─────┘
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    1
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

提示：
* 链表中节点的数目范围在范围 [0, 10^4] 内
* -10^5 <= Node.val <= 10^5
* pos 的值为 -1 或者链表中的一个有效索引

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针，两个指针从头开始向后移动，慢指针每次移动1格，快指针每次移动2格，如果两者相遇则表示有环
        # 在相遇时使用第三个指针从头开始移动，每次一格，之前的慢指针同时继续移动，两者相遇的位置即为环的开始节点
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:  # 找到环
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(3)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(0)
    curNode.next = curNode = ListNode(-4)
    curNode.next = head.next
    r = s.detectCycle(head)
    print(r.val if r else None)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = head
    r = s.detectCycle(head)
    print(r.val if r else None)

    head = ListNode(1)
    r = s.detectCycle(head)
    print(r.val if r else None)
