"""
基础数据结构

本单元包含题目中常见的通用数据结构，如：链表、树等
"""

from collections import deque
from typing import List


NULL_STR = 'null'  # 空节点打印的字符串


# region 单向链表

class ListNode:
    """ 单向链表 """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(node: ListNode):
    """ 打印链表 """
    if node is None:
        print(NULL_STR)
    else:
        while node:
            print(node.val, end=', ')
            node = node.next
        print()

# endregion


# region 二叉树

class TreeNode:
    """ 二叉树节点 """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root: TreeNode):
    """ 打印树 """
    nodeStrs = []
    nodes = deque((root,))
    while nodes:
        node = nodes.popleft()
        if node is None:
            nodeStrs.append(NULL_STR)
        else:
            nodeStrs.append(str(node.val))
            nodes.append(node.left)
            nodes.append(node.right)
    while nodeStrs and nodeStrs[-1] == NULL_STR:  # 移除最后的空节点
        nodeStrs.pop()
    print(', '.join(nodeStrs))


def printTrees(trees: List[TreeNode]):
    """ 打印一组树 """
    print('[')
    for i, tree in enumerate(trees):
        print('  ', end='')
        printTree(tree)
    print(']')

# endregion
