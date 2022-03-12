"""
扁平化多级双向链表

多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。
这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

示例 1：
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：
输入的多级列表如下图所示：
  1 --- 2 --- 3 --- 4 --- 5 --- 6 --- NULL
              |
              7 --- 8 --- 9 --- 10 --- NULL
                    |
                   11 --- 12 --- NULL
扁平化后的链表如下图：
  1 --- 2 --- 3 --- 7 --- 8 --- 11 --- 12 --- 9 --- 10 --- 4 --- 5 --- 6 --- NULL

示例 2：
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：
输入的多级列表如下图所示：
  1---2---NULL
  |
  3---NULL

示例 3：
输入：head = []
输出：[]

如何表示测试用例中的多级链表？
以 示例 1 为例：
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
序列化其中的每一级之后：
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
合并所有序列化结果，并去除末尾的 null 。
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

提示：
* 节点数目不超过 1000
* 1 <= Node.val <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:

        def flatternOneLayer(node: Node) -> Node:
            """ 扁平化一层链表
            :returns: 返回链表尾节点
            """
            while True:
                if node.child:
                    tail, nextNode = flatternOneLayer(node.child), node.next
                    node.next, node.child.prev = node.child, node
                    if nextNode:
                        nextNode.prev = tail
                    tail.next, node.child, node = nextNode, None, tail
                if not node.next:
                    return node
                node = node.next

        if head:
            flatternOneLayer(head)
        return head


def printList(node: Node):
    """ 打印链表 """
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


if __name__ == '__main__':
    s = Solution()

    head = curNode = Node(1, None, None, None)
    curNode.next = curNode = Node(2, curNode, None, None)
    curNode.next = curNode = Node(3, curNode, None, None)
    curNode.next = curNode = Node(4, curNode, None, None)
    curNode.next = curNode = Node(5, curNode, None, None)
    curNode.next = curNode = Node(6, curNode, None, None)
    head.next.next.child = curNode = Node(7, None, None, None)
    curNode.next = curNode = Node(8, curNode, None, None)
    curNode.next = curNode = Node(9, curNode, None, None)
    curNode.next = curNode = Node(10, curNode, None, None)
    head.next.next.child.next.child = curNode = Node(11, None, None, None)
    curNode.next = curNode = Node(12, curNode, None, None)
    r = s.flatten(head)
    printList(r)

    head = curNode = Node(1, None, None, None)
    curNode.next = curNode = Node(2, curNode, None, None)
    head.child = Node(3, None, None, None)
    r = s.flatten(head)
    printList(r)

    r = s.flatten(None)
    printList(r)
