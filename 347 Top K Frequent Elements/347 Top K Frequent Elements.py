# Best Leetcode problems for FAANG: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986
# Youtube solution: https://www.youtube.com/watch?v=QubWUx59QCk
# Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/0


from collections import Counter
import heapq


def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    count = Counter(nums)

    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    print(heap)

    return [num for _, num in heap]

# def topKFrequent(nums, k):
#     count = Counter(nums)  # Step 1: Count frequencies
#     sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)  # Step 2: Sort by frequency
#     return sorted_elements[:k]  # Step 3: Get the top K elements


# Example usage:
nums = [2, 2, 3, 1, 1, 1]
k = 2
print(topKFrequent(nums, k))  # Output: [1,2]
