# LeetCode Link (242. Valid Anagram): https://leetcode.com/problems/valid-anagram/
# Youtube Solution: https://youtu.be/qyQni3rz-ko

#  Anagram strings: if both string contains same count of each characters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in count)

    def isAnagramUsingHash(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        # Count frequency of characters in 's'
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Subtract frequency using characters in 't'
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False  # Extra character found in 't'

        # Check if all frequencies are zero
        for value in freq.values():
            if value != 0:
                return False

        return True


s = Solution()
print(s.isAnagram("problem", "rpolbme"))

#  time- > 0(n)
#  space -> 0(1)
