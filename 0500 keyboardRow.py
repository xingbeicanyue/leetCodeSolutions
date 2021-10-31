"""
键盘行

给你一个字符串数组 words ，只返回可以使用在美式键盘同一行的字母打印出来的单词。

美式键盘中：
* 第一行由字符 "qwertyuiop" 组成。
* 第二行由字符 "asdfghjkl" 组成。
* 第三行由字符 "zxcvbnm" 组成。

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

提示：
* 1 <= words.length <= 20
* 1 <= words[i].length <= 100
* words[i] 由英文字母（小写和大写字母）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表、字符串
"""

from typing import List


class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        # 打表法，构造每个字母对应的行号，检查单词中所有字母是否对应同一行号
        charRowDict = {
            'q': 0, 'Q': 0, 'w': 0, 'W': 0, 'e': 0, 'E': 0, 'r': 0, 'R': 0, 't': 0, 'T': 0, 'y': 0, 'Y': 0,
            'u': 0, 'U': 0, 'i': 0, 'I': 0, 'o': 0, 'O': 0, 'p': 0, 'P': 0, 'a': 1, 'A': 1, 's': 1, 'S': 1,
            'd': 1, 'D': 1, 'f': 1, 'F': 1, 'g': 1, 'G': 1, 'h': 1, 'H': 1, 'j': 1, 'J': 1, 'k': 1, 'K': 1,
            'l': 1, 'L': 1, 'z': 2, 'Z': 2, 'x': 2, 'X': 2, 'c': 2, 'C': 2, 'v': 2, 'V': 2, 'b': 2, 'B': 2,
            'n': 2, 'N': 2, 'm': 2, 'M': 2
        }
        result = []
        for word in words:
            row = charRowDict[word[0]]
            for i in range(1, len(word)):
                if charRowDict[word[i]] != row:
                    break
            else:
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.findWords(['Hello', 'Alaska', 'Dad', 'Peace'])
    print(r)

    r = s.findWords(['omk'])
    print(r)

    r = s.findWords(['adsdf', 'sfd'])
    print(r)
