"""
找到字符串中所有字母异位词

给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
* 字母异位词指字母相同，但排列不同的字符串。
* 不考虑答案输出的顺序。

示例 1:
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

示例 2:
输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口，当遇到不需要的字符时可以直接跳过整个窗口
        sLen, pLen = len(s), len(p)
        if sLen < pLen:
            return []
        result = []
        pCharCounter, sCharCounter = Counter(p), Counter(s[:pLen])
        if pCharCounter == sCharCounter:
            result.append(0)
        leftIdx, rightIdx = 0, pLen  # 滑动窗口左|右侧下标
        while rightIdx < sLen:
            if s[rightIdx] not in pCharCounter:
                leftIdx = rightIdx + 1
                rightIdx = leftIdx + pLen
                sCharCounter = Counter(s[leftIdx: rightIdx])
            else:
                if rightIdx - leftIdx >= pLen:
                    leftChar = s[leftIdx]
                    sCharCounter.subtract(leftChar)
                    if sCharCounter[leftChar] == 0:
                        del sCharCounter[leftChar]
                    leftIdx += 1
                sCharCounter.update(s[rightIdx])
                rightIdx += 1
            if sCharCounter == pCharCounter:
                result.append(leftIdx)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findAnagrams('cbaebabacd', 'abc')
    print(r)
    r = s.findAnagrams('abab', 'ab')
    print(r)
