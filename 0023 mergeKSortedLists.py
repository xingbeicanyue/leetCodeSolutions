"""
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

提示：
* k == lists.length
* 0 <= k <= 10^4
* 0 <= lists[i].length <= 500
* -10^4 <= lists[i][j] <= 10^4
* lists[i] 按升序排列
* lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：堆、链表、分治算法
"""

from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 方法1：优先队列
        # 不修改节点数据，不创建新节点
        queue, curNodes = PriorityQueue(), lists[:]  # 优先队列 | [每条链表即将访问的节点]
        for i, node in enumerate(lists):
            if node is not None:
                queue.put((node.val, i))
        result = resultTail = ListNode(0)
        while queue.qsize() > 0:
            curNodeIdx = queue.get()[1]
            curNode = curNodes[curNodeIdx]
            resultTail.next = resultTail = curNode
            if curNode.next is not None:
                queue.put((curNode.next.val, curNodeIdx))
                curNodes[curNodeIdx] = curNode.next
        return result.next


        # 方法2：分治
        # def merge(node1: ListNode, node2: ListNode) -> ListNode:
        #     result = resultTail = ListNode(0)
        #     while node1 and node2:
        #         if node1.val <= node2.val:
        #             resultTail.next = resultTail = node1
        #             node1 = node1.next
        #         else:
        #             resultTail.next = resultTail = node2
        #             node2 = node2.next
        #     resultTail.next = node1 if node1 else node2
        #     return result.next
        #
        # nodes = lists[:]
        # while len(nodes) > 1:
        #     nextNodes = []
        #     for i in range(0, len(nodes), 2):
        #         if i + 1 >= len(nodes):
        #             nextNodes.append(nodes[i])
        #             continue
        #         nextNodes.append(merge(nodes[i], nodes[i + 1]))
        #     nodes = nextNodes
        # return nodes[0] if nodes else None


def printList(node: ListNode):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()
    lists = []
    node1 = curNode = ListNode(1)
    curNode.next = curNode = ListNode(4)
    curNode.next = curNode = ListNode(5)
    lists.append(node1)
    node2 = curNode = ListNode(1)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    lists.append(node2)
    node3 = curNode = ListNode(2)
    curNode.next = curNode = ListNode(6)
    lists.append(node3)
    r = s.mergeKLists(lists)
    printList(r)

    r = s.mergeKLists([])
    printList(r)

    r = s.mergeKLists([None])
    printList(r)
