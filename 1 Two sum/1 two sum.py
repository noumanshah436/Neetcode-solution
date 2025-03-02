# https://leetcode.com/problems/two-sum/description/
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum(nums, target):
    """
    Finds two numbers in the list that add up to the target and returns their indices.

    :param nums: List[int] - A list of integers
    :param target: int - The target sum
    :return: List[int] - A list containing the indices of the two numbers
    """

    # Dictionary to store {number: index} pairs
    num_to_index = {}

    # Iterate over the list with index and value
    for index, number in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - number

        # If the complement exists in the dictionary, return the indices
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Store the current number and its index in the dictionary
        num_to_index[number] = index

    # If no solution is found, return an empty list (shouldn't happen as per problem constraints)
    return []


# Example usage
print(twoSum([7, 11, 2, 15], target=9))  # Output: [2, 0]



# The function uses a hashmap (dict) to store visited numbers and their indices, checking for each number if its complement 
# (target - number) exists in the hashmap to return the matching indices in O(n) time complexity.