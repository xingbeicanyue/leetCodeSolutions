"""
循环有序列表的插入

给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

示例 1：
  3 -> 4 -> 1
  ^         |
  |---------| 
输入：head = [3,4,1], insertVal = 2
输出：[3,4,1,2]
解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。
     新插入的节点应该在 1 和 3 之间，插入之后，整个列表如下图所示，最后返回节点 3 。
  3 -> 4 -> 1 -> 2
  ^              |
  |--------------| 

示例 2：
输入：head = [], insertVal = 1
输出：[1]
解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。

示例 3：
输入：head = [1], insertVal = 0
输出：[1,0]

提示：
0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：链表
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        # 遍历链表
        # 若插入值在链表值域区间内，则遍历时会在两个相邻节点处插入，否则在链表唯一一处降序处插入，若链表所有值都一样则随意插入

        if head is None:
            result = Node(insertVal)
            result.next = result
            return result
        curNode = head
        while True:
            if curNode.next.val >= curNode.val:
                if curNode.val <= insertVal <= curNode.next.val:  # 插入值在两个升序节点值中间
                    break
            elif insertVal >= curNode.val or insertVal <= curNode.next.val:  # 插入值比链表中所有值都大/小，插入在降序处
                break
            if curNode.next == head:  # 链表中所有值都一样，且与插入值不同
                break
            curNode = curNode.next
        # 在curNode与curNode.next间插入
        insertNode = Node(insertVal)
        curNode.next, insertNode.next = insertNode, curNode.next
        return head


def printCircularList(node: Node):
    """ 打印循环链表 """
    printeds = set()
    while node and node not in printeds:
        printeds.add(node)
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = Node(3)
    curNode.next = curNode = Node(4)
    curNode.next = curNode = Node(1)
    curNode.next = head
    r = s.insert(head, 2)
    printCircularList(r)

    r = s.insert(None, 1)
    printCircularList(r)

    head = Node(1)
    head.next = head
    r = s.insert(head, 0)
    printCircularList(r)
