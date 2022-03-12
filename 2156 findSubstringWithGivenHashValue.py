"""
查找给定哈希值的子串

给定整数 p 和 m，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算：
hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) * p^(k-1)) mod m.
其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26。

给你一个字符串 s 和整数 power，modulo，k 和 hashValue。
请你返回 s 中第一个长度为 k 的子串 sub ，满足 hash(sub, power, modulo) == hashValue。
测试数据保证一定存在至少一个这样的子串。
子串定义为一个字符串中连续非空字符组成的序列。

示例 1：
输入：s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
输出："ee"
解释："ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
"ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。

示例 2：
输入：s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
输出："fbx"
解释："fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 31^2) mod 100 = 23132 mod 100 = 32 。
"bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 31^2) mod 100 = 25732 mod 100 = 32 。
"fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。
注意，"bxz" 的哈希值也为 32，但是它在字符串中比 "fbx" 更晚出现。

提示：
* 1 <= k <= s.length <= 2 * 10^4
* 1 <= power, modulo <= 10^9
* 0 <= hashValue < modulo
* s 只包含小写英文字母。
* 测试数据保证一定存在满足条件的子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-substring-with-given-hash-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        # 直接计算数值会很大，因此考虑将取模分解
        # 计算出 p的0 ~ k-1次方的幂对于m的模为M(i)
        # 则hash(s,p,m) = Σ(M(i)*s[i]) % m
        # 对于起始下标为i的子串来说有 hash(s,p,m,i) = ((hash(s,p,m,i+1) - M(k-1)*s[i+k])*p + s[i]) % m

        # 计算p的0 ~ k-1次方的幂对于modulo的模 -> powerModules
        powerModules = [1]  # [power^i%modulo]
        for i in range(k - 1):
            powerModules.append(powerModules[-1] * power % modulo)
        # 从后往前遍历子串
        resultSIdx = 0
        base = ord('a') - 1
        sLen = len(s)
        curValue = sum((ord(s[i]) - base) * powerModules[i - sLen + k] for i in range(sLen - k, sLen)) % modulo
        if curValue == hashValue:
            resultSIdx = sLen - k
        for i in range(sLen - k - 1, -1, -1):
            curValue = ((curValue - (ord(s[i + k]) - base) * powerModules[-1]) * power + (ord(s[i]) - base)) % modulo
            if curValue == hashValue:
                resultSIdx = i
        return s[resultSIdx: resultSIdx + k]


if __name__ == '__main__':
    s = Solution()

    r = s.subStrHash('leetcode', 7, 20, 2, 0)
    print(r)

    r = s.subStrHash('fbxzaad', 31, 100, 3, 32)
    print(r)
