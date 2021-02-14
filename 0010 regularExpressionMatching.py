"""
正则表达式匹配

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
* '.' 匹配任意单个字符
* '*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串 s 的，而不是部分字符串。

示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false

提示：
* 0 <= s.length <= 20
* 0 <= p.length <= 30
* s 可能为空，且只包含从 a-z 的小写字母。
* p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
* 保证每次出现字符 * 时，前面都匹配到有效的字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、动态规划、回溯算法
"""

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def match(sIdx: int, pIdx: int) -> bool:
            """ 返回s[sIdx:]是否匹配p[pIdx:] """
            if sIdx >= sLen and pIdx >= pLen:
                return True
            if pIdx >= pLen:
                return False
            # 计算待匹配字符与个数 -> pc, isAny
            pc, isAny = p[pIdx], False  # 待匹配的字符 | 是否匹配任意多个字符
            pIdx += 1
            if pIdx < pLen and p[pIdx] == '*':
                isAny = True
                pIdx += 1
            # 匹配
            if isAny:
                if match(sIdx, pIdx):
                    return True
                for i in range(sIdx, sLen):
                    if s[i] == pc or pc == '.':
                        if match(i + 1, pIdx):
                            return True
                    else:
                        break
                return False
            else:
                return sIdx < sLen and (s[sIdx] == pc or pc == '.') and match(sIdx + 1, pIdx)

        sLen, pLen = len(s), len(p)
        return match(0, 0)


if __name__ == '__main__':
    s = Solution()
    r = s.isMatch('aa', 'a')
    print(r)
    r = s.isMatch('aa', 'a*')
    print(r)
    r = s.isMatch('ab', '.*')
    print(r)
    r = s.isMatch('aab', 'c*a*b')
    print(r)
    r = s.isMatch('mississippi', 'mis*is*p*.')
    print(r)
