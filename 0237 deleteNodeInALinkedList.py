"""
删除链表中的节点

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为要被删除的节点。
现有一个链表 -- head = [4,5,1,9]，它可以表示为:
  4 -> 5 -> 1 -> 9

示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

提示：
* 链表至少包含两个节点。
* 链表中所有节点的值都是唯一的。
* 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
* 不要从你的函数中返回任何结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        # 将下一个节点的值赋予被删除的节点并移除下一个节点
        node.val = node.next.val
        node.next = node.next.next


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(4)
    curNode.next = curNode = param = ListNode(5)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(9)
    s.deleteNode(param)
    printList(head)

    head = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    curNode.next = curNode = param = ListNode(1)
    curNode.next = curNode = ListNode(9)
    s.deleteNode(param)
    printList(head)
