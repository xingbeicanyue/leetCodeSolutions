"""
串联所有单词的子串

给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表、双指针、字符串
"""

from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        result, wordLen = [], len(words[0])
        for i in range(wordLen):  # 每次循环从i开始，以wordLen为宽度截取单词，用滑动窗口的方式遍历单词
            missCount = len(words)  # 未匹配的单词数
            missWordCounter = defaultdict(int)  # 未匹配的单词及个数
            for word in words:
                missWordCounter[word] += 1
            leftIdx = i
            for rightIdx in range(i, len(s), wordLen):
                word = s[rightIdx: rightIdx + wordLen]
                missWordCounter[word] -= 1
                if missWordCounter[word] >= 0:
                    if missCount == 1:  # 全部匹配
                        result.append(leftIdx)
                        missWordCounter[s[leftIdx: leftIdx + wordLen]] += 1
                        leftIdx += wordLen
                    else:
                        missCount -= 1
                else:  # 遇到不需要匹配的单词，滑动窗口左侧使该单词离开窗口
                    while leftIdx < len(s):
                        word2 = s[leftIdx: leftIdx + wordLen]
                        missWordCounter[word2] += 1
                        leftIdx += wordLen
                        if word2 == word:
                            break
                        missCount += 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.findSubstring('barfoothefoobarman', ['foo', 'bar'])
    print(r)
    r = s.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word'])
    print(r)
