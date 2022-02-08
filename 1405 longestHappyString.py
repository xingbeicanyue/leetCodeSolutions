"""
最长快乐字符串

如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
给你三个整数 a，b ，c，请你返回任意一个满足下列全部条件的字符串 s：
* s 是一个尽可能长的快乐字符串。
* s 中 最多 有 a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
* s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

示例 1：
输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。

示例 2：
输入：a = 2, b = 2, c = 1
输出："aabbc"

示例 3：
输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。

提示：
* 0 <= a, b, c <= 100
* a + b + c > 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-happy-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心、字符串、堆
"""

from heapq import heapify, heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 每次取数量最多的字母，如果组成连续3个相同字母则取次多的字母，直至无字母可取

        resultChars = ['d', 'd']  # 'd'为哨兵
        heap = [[-a, 'a'], [-b, 'b'], [-c, 'c']]  # 小顶堆，用负数排序
        heapify(heap)

        def addMostChar(checkSame: bool) -> bool:
            """ 在resultChars中添加heap中数量最多的字母
            :param checkSame: 是否检查连续3个相同字母
            :return: 返回是否成功添加
            """
            if len(heap) == 0:
                return False
            curChar = heappop(heap)
            if curChar[0] == 0:
                return False
            if checkSame and curChar[1] == resultChars[-1] == resultChars[-2]:
                result = addMostChar(False)
            else:
                resultChars.append(curChar[1])
                curChar[0] += 1
                result = True
            heappush(heap, curChar)
            return result

        while addMostChar(True):
            pass
        return ''.join(resultChars[2:])


if __name__ == '__main__':
    s = Solution()

    r = s.longestDiverseString(1, 1, 7)
    print(r)

    r = s.longestDiverseString(2, 2, 1)
    print(r)

    r = s.longestDiverseString(7, 1, 0)
    print(r)
