"""
回文链表

请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 找到中间节点
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                slow, fast = slow.next, fast.next
        # 反转后半段链表
        curNode, slow.next = slow.next, None
        while curNode:
            curNode.next, curNode, slow = slow, curNode.next, curNode
        # 逐一比较
        left, right, result = head, slow, True
        while right:  # 不可用left判断，因为当节点数为偶数时，左链表会多一个节点
            if left.val != right.val:
                result = False
                break
            left, right = left.next, right.next
        # 若不希望链表被修改则需恢复链表
        return result


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    r = s.isPalindrome(head)
    print(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(1)
    r = s.isPalindrome(head)
    print(r)
