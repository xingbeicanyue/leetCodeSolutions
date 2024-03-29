"""
环形链表

给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。否则，返回 false 。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？

示例 1：
    3 --> 2 --> 0 --> -4
          ^            │
          └────────────┘
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    1 --> 2
    ^     │
    └─────┘
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    1
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 
提示：
* 链表中节点的数目范围是 [0, 10^4]
* -10^5 <= Node.val <= 10^5
* pos 为 -1 或者链表中的一个有效索引。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(3)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(0)
    curNode.next = curNode = ListNode(-4)
    curNode.next = head.next
    r = s.hasCycle(head)
    print(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = head
    r = s.hasCycle(head)
    print(r)

    head = ListNode(1)
    r = s.hasCycle(head)
    print(r)
