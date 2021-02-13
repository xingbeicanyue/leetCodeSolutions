"""
单词拆分

给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
* 拆分时可以重复使用字典中的单词。
* 你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：动态规划
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False
        canBreaks = [False] * (len(s) + 1)  # s[:i]是否能拆分
        canBreaks[0] = True
        maxWordLen = max(len(word) for word in wordDict)
        for i in range(len(s)):
            for j in range(max(0, i - maxWordLen + 1), i + 1):
                if canBreaks[j] and s[j: i + 1] in wordDict:
                    canBreaks[i + 1] = True
                    break
        return canBreaks[-1]


if __name__ == '__main__':
    s = Solution()
    r = s.wordBreak('leetcode', ['leet', 'code'])
    print(r)
    r = s.wordBreak('applepenapple', ['apple', 'pen'])
    print(r)
    r = s.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])
    print(r)
