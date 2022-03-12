"""
重复的DNA序列

DNA序列由一系列核苷酸组成，缩写为'A','C','G'和'T'.。
例如，"ACGAATTCCG"是一个 DNA序列 。
在研究 DNA 时，识别 DNA 中的重复序列非常有用。
给定一个表示DNA序列的字符串 s ，返回所有在 DNA 分子中出现不止一次的长度为10的序列(子字符串)。你可以按任意顺序返回答案。

示例 1：
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

示例 2：
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]

提示：
* 0 <= s.length <= 10^5
* s[i]=='A'、'C'、'G' or 'T'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 滚动哈希算法（Rabin-Karp）
        if len(s) <= 10:
            return []
        charIntDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        hashValCountDict = {}  # {哈希值: [字符串终止下标, 次数]}
        hashVal = sum(charIntDict[s[i]] * (4 ** (9 - i)) for i in range(10))
        hashValCountDict[hashVal] = [9, 1]
        hashRate = 4 ** 10
        for i in range(10, len(s)):
            hashVal = hashVal * 4 - charIntDict[s[i - 10]] * hashRate + charIntDict[s[i]]
            if hashVal in hashValCountDict:
                hashValCountDict[hashVal][1] += 1
            else:
                hashValCountDict[hashVal] = [i, 1]
        return [s[strCount[0] - 9: strCount[0] + 1] for strCount in hashValCountDict.values() if strCount[1] > 1]


if __name__ == '__main__':
    s = Solution()

    r = s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print(r)

    r = s.findRepeatedDnaSequences('AAAAAAAAAAAAA')
    print(r)
