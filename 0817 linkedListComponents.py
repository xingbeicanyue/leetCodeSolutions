"""
链表组件

给定链表头结点 head，该链表上的每个结点都有一个唯一的整型值。
同时给定列表 G，该列表是上述链表中整型值的一个子集。
返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。

示例 1：
输入:
head: 0->1->2->3
G = [0, 1, 3]
输出: 2
解释:
链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。

示例 2：
输入:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
输出: 2
解释:
链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。

提示：
* 如果 N 是给定链表 head 的长度，1 <= N <= 10000。
* 链表中每个结点的值所在范围为 [0, N - 1]。
* 1 <= G.length <= 10000
* G 是链表中所有结点的值的一个子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-components
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # 将G变为集合方便判断数值是否在G中
        # 遍历链表，如果数值在G中则表示形成了组件，添加标记；若不在G中且形成了组件则将结果+1，清空标记
        result, values = 0, set(G)
        hasComponent = False  # 是否形成组件
        while head:
            if head.val in values:
                hasComponent = True
            else:
                result += hasComponent
                hasComponent = False
            head = head.next
        return result + hasComponent


if __name__ == '__main__':
    s = Solution()

    head = curNode = ListNode(0)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    r = s.numComponents(head, [0, 1, 3])
    print(r)

    head = curNode = ListNode(0)
    curNode.next = curNode = ListNode(1)
    curNode.next = curNode = ListNode(2)
    curNode.next = curNode = ListNode(3)
    curNode.next = curNode = ListNode(4)
    r = s.numComponents(head, [0, 3, 1, 4])
    print(r)
