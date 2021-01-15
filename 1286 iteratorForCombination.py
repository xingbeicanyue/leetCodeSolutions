"""
字母组合迭代器

请你设计一个迭代器类，包括以下内容：
* 一个构造函数，输入参数包括：
  一个有序且字符唯一的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。
* 函数 next() ，按字典序返回长度为 combinationLength 的下一个字母组合。
* 函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。
 
示例：
CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator
iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false
 
提示：
* 1 <= combinationLength <= characters.length <= 15
* 每组测试数据最多包含 10^4 次函数调用。
* 题目保证每次调用函数 next 时都存在下一个字母组合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/iterator-for-combination
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：设计、回溯算法
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._characters = characters
        self._length = combinationLength
        self._characterIdxs = [i for i in range(combinationLength)]

    def next(self) -> str:
        result = ''.join(self._characters[idx] for idx in self._characterIdxs)
        self._doIter()
        return result

    def hasNext(self) -> bool:
        return self._characterIdxs is not None

    def _doIter(self):
        """ 迭代至下一个值 """
        while self._characterIdxs:
            nextIdx = self._characterIdxs.pop() + 1
            characterLackCount = self._length - len(self._characterIdxs)
            if len(self._characters) - nextIdx >= characterLackCount:
                self._characterIdxs += [i for i in range(nextIdx, nextIdx + characterLackCount)]
                return
        else:
            self._characterIdxs = None


if __name__ == '__main__':
    iterator = CombinationIterator('abc', 2)
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
