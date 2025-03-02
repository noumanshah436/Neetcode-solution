# Leetcode Link: https://leetcode.com/problems/group-anagrams/
# Youtube Solution: https://www.youtube.com/watch?v=dEMcIpBOHpg

from collections import defaultdict


class Solution(object):

    from collections import defaultdict

    def groupAnagrams(self, strs):
        if not strs:
            return []

        # Dictionary to store grouped anagrams
        # The key will be a unique representation of character counts
        # The value will be a list of words that match this key
        ans_map = defaultdict(list)

        # Iterate through each word in the input list
        for s in strs:
            # Create a frequency array to count occurrences of each letter (a-z)
            # Since there are 26 letters in the English alphabet
            count = [0] * 26

            # Count the occurrences of each character in the word
            for c in s:
                # Convert character to index (0-25) and increment count
                count[ord(c) - ord('a')] += 1

            # Convert the count list to a unique key
            # This ensures that words with the same character frequencies get the same key
            key = tuple(count)

            # Append the word to the corresponding group in the dictionary
            ans_map[key].append(s)

        # Return all grouped anagrams as a list of lists
        return list(ans_map.values())

    # def groupAnagrams(self, strs):
    #     if len(strs) == 0:
    #         return []

    #     # Create a dictionary to store anagrams
    #     anagram_dict = {}

    #     # Iterate over each string in the list
    #     for s in strs:
    #         # Sort the characters in the string
    #         sorted_s = ''.join(sorted(s))

    #         # If the sorted string is already in the dictionary, add the current string to the list
    #         if sorted_s in anagram_dict:
    #             anagram_dict[sorted_s].append(s)
    #         # If the sorted string is not in the dictionary, create a new list with the current string
    #         else:
    #             anagram_dict[sorted_s] = [s]

    #     # Convert the dictionary values (lists of anagrams) to lists of lists (groups of anagrams)
    #     return list(anagram_dict.values())


# Test the solution

# strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["bdddddddddd", "bbbbbbbbbbc"]


s = Solution()
print(s.groupAnagrams(strs))
