"""
设计循环双端队列

设计实现双端队列。
你的实现需要支持以下操作：
* MyCircularDeque(k)：构造函数,双端队列的大小为k。
* insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
* insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
* deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
* deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
* getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
* getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
* isEmpty()：检查双端队列是否为空。
* isFull()：检查双端队列是否满了。

示例：
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			                // 返回 true
circularDeque.insertLast(2);			                // 返回 true
circularDeque.insertFront(3);			                // 返回 true
circularDeque.insertFront(4);			                // 已经满了，返回 false
circularDeque.getRear();  				                // 返回 2
circularDeque.isFull();				                    // 返回 true
circularDeque.deleteLast();			                    // 返回 true
circularDeque.insertFront(4);			                // 返回 true
circularDeque.getFront();			                	// 返回 4
 
提示：
* 所有值的范围为 [1, 1000]
* 操作次数的范围为 [1, 1000]
* 请不要使用内置的双端队列库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-circular-deque
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self._maxCount = k
        self._queue = [0] * k
        self._sIdx = 0
        self._count = 0

    def insertFront(self, value: int) -> bool:
        if self._count == self._maxCount:
            return False
        self._sIdx = (self._sIdx - 1) % self._maxCount
        self._queue[self._sIdx] = value
        self._count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self._count == self._maxCount:
            return False
        self._queue[(self._sIdx + self._count) % self._maxCount] = value
        self._count += 1
        return True

    def deleteFront(self) -> bool:
        if self._count == 0:
            return False
        self._sIdx = (self._sIdx + 1) % self._maxCount
        self._count -= 1
        return True

    def deleteLast(self) -> bool:
        if self._count == 0:
            return False
        self._count -= 1
        return True

    def getFront(self) -> int:
        return self._queue[self._sIdx] if self._count > 0 else -1

    def getRear(self) -> int:
        return self._queue[(self._sIdx + self._count - 1) % self._maxCount] if self._count > 0 else -1

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._maxCount


if __name__ == '__main__':
    deque = MyCircularDeque(3)
    print(deque.insertLast(1))
    print(deque.insertLast(2))
    print(deque.insertFront(3))
    print(deque.insertFront(4))
    print(deque.getRear())
    print(deque.isFull())
    print(deque.deleteLast())
    print(deque.insertFront(4))
    print(deque.getFront())
