"""
基础数据结构

本单元包含题目中常见的通用数据结构，如：链表、树等
"""


class ListNode:
    """ 单向链表 """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(node: ListNode):
    """ 打印链表 """
    if node is None:
        print('empty list')
    else:
        while node:
            print(node.val, end=', ')
            node = node.next
        print()
