"""
删除排序链表中的重复元素

存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素只出现一次。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
* 链表中节点数目在范围 [0, 300] 内
* -100 <= Node.val <= 100
* 题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 遍历链表，若相邻节点值相等则移除后一个节点
        if head is None:
            return None
        curNode = head
        while curNode.next is not None:
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    r = s.deleteDuplicates(head)
    printList(r)

    head = curNode = ListNode(1)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(3)
    r = s.deleteDuplicates(head)
    printList(r)
