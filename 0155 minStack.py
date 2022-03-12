"""
最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
* MinStack() 初始化堆栈对象。
* void push(int val) 将元素val推入堆栈。
* void pop() 删除堆栈顶部的元素。
* int top() 获取堆栈顶部的元素。
* int getMin() 获取堆栈中的最小元素。

示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]
解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：
* -2^31 <= val <= 2^31 - 1
* pop、top 和 getMin 操作总是在非空栈上调用
* push, pop, top, and getMin最多被调用 3 * 10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MinStack:

    def __init__(self):
        self._stack = []
        self._minValStack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._minValStack or x <= self._minValStack[-1]:
            self._minValStack.append(x)

    def pop(self) -> None:
        if self._stack[-1] == self._minValStack[-1]:
            self._minValStack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minValStack[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
