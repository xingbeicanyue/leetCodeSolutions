"""
给单链表加一

用一个非空单链表来表示一个非负整数，然后将这个整数加一。
你可以假设这个整数除了 0 本身，没有任何前导的 0。
这个整数的各个数位按照高位在链表头部、低位在链表尾部的顺序排列。

示例:
输入: [1,2,3]
输出: [1,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # 遍历链表，在尾节点+1，反向遍历逐次判断是否进位
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        for node in reversed(nodes):
            if node.val < 9:
                node.val += 1
                break
            node.val = 0
        else:
            return ListNode(1, nodes[0])
        return nodes[0]


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
    r = s.plusOne(head)
    printList(r)
