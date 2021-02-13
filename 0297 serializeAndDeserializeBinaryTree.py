"""
二叉树的序列化与反序列化

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例 1：
    1
  ┌─┴─┐
  2   3
    ┌─┴─┐
    4   5
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

提示：
* 树中结点数在范围 [0, 10^4] 内
* -1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：树、设计
"""

from collections import deque


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        # 按层次遍历的顺序序列化
        result, noneCount = [], 0
        nodeQueue = deque()
        nodeQueue.append(root)
        while nodeQueue:
            node = nodeQueue.popleft()
            if node is None:  # 延迟加入空值，因为最终结果不包含最后的空值
                noneCount += 1
            else:
                if noneCount > 0:
                    result.extend(['n'] * noneCount)
                    noneCount = 0
                result.append(str(node.val))
                nodeQueue.append(node.left)
                nodeQueue.append(node.right)
        return ','.join(result)

    def deserialize(self, data):
        if len(data) == 0:
            return None
        values = data.split(',')
        root = TreeNode(int(values[0]))
        nodeQueue = deque()
        nodeQueue.append(root)
        i, length = 0, len(values)
        for i in range(1, length, 2):
            node = nodeQueue.popleft()
            if values[i] != 'n':
                node.left = TreeNode(int(values[i]))
                nodeQueue.append(node.left)
            if i + 1 < length and values[i + 1] != 'n':
                node.right = TreeNode(int(values[i + 1]))
                nodeQueue.append(node.right)
        return root


if __name__ == '__main__':
    ser = Codec()
    deser = Codec()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5
    r = ser.serialize(deser.deserialize(ser.serialize(node1)))
    print(r)

    r = ser.serialize(deser.deserialize(ser.serialize(None)))
    print(r)

    node1 = TreeNode(1)
    r = ser.serialize(deser.deserialize(ser.serialize(node1)))
    print(r)

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2
    r = ser.serialize(deser.deserialize(ser.serialize(node1)))
    print(r)
