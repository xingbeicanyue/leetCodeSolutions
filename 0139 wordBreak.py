"""
单词拆分

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

提示：
* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* 1 <= wordDict[i].length <= 20
* s 和 wordDict[i] 仅有小写英文字母组成
* wordDict 中的所有字符串互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # 对于字符串s，拆分为a+b，若a可拼接，且b在字典中，则s可拼接
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
