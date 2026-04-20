# Original problem with examples
# 📝 Problem: Merge Intervals
# Given a collection of intervals, merge all overlapping intervals. For example, if you have the intervals [(1, 3), (2, 4), (5, 7)], they should be merged into [(1, 4), (5, 7)].
# Input:
# A list of n intervals where each interval is represented as a tuple (start, end).
# Output:
# A list of merged intervals.
# Constraints:
# 1 ≤ n ≤ 10⁴
# 0 ≤ start ≤ end ≤ 10⁶
# 📥 Example 1
# Input:
# intervals = [(1, 3), (2, 4), (5, 7), (6, 8)]
#
# Output:
# [(1, 4), (5, 8)]
# 📥 Example 2
# Input:
# intervals = [(1, 4), (2, 3), (5, 7)]
#
# Output:
# [(1, 4), (5, 7)]
# 📥 Example 3
# Input:
# intervals = [(1, 5), (6, 8), (7, 9)]
#
# Output:
# [(1, 5), (6, 9)]
# ⚠️ Requirements
# Merge intervals with O(n log n) time complexity. Sorting is likely involved.
# Consider edge cases like:
# Empty list.
# Intervals that don’t overlap at all.
# Multiple intervals overlapping.

# Restate the Problem:
# A list of tuples are given [(start, end)], find the overlapping tuples and merge them

# Approach:
# - What data structure(s) am I using?: just lists

# - What algorithm/paradigm? A simple sort (python function)
# - This is a list of lists that will be sorted by start value from least to greatest
# - Check each value and merge in n time

# Variables:
# - tuple_index: int
# - current_start: int
# - current_end: int
# - tuple_start: int
# - future_tuple_start: int
# - new_tuple_list: list[list[int]]

# Steps:
# - check if list is empty
# - sort the list of tuples
# - loop through list of tuples
# - check if current_tuple[0] (start interval) is greater than current_end
#   - make current_start and current_end its own tuple and add it to a new list
#   - set current_start and current_end based off of current_tuple
# - else (since current_end is greater) check the end of the current tuple
# - if it is greater, then set the current_end to current_tuple[1]
# - else

# Time Complexity:
# - O(n log (n)) due to the sort

# Space Complexity:
# - O(n)


def merge_intervals(tuple_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(tuple_list) == 0:
        return []
    elif len(tuple_list) == 1:
        return tuple_list

    tuple_list.sort(key = lambda x: x[0])

    new_tuple_list: list[tuple[int, int]] = []

    current_start: int = tuple_list[0][0]
    current_end: int = tuple_list[0][1]

    start_index: int = 1
    for index in range(start_index, len(tuple_list)):
        if current_end < tuple_list[index][0]:
            new_tuple: tuple[int, int] = (current_start, current_end)
            new_tuple_list.append(new_tuple)
            current_start = tuple_list[index][0]
            current_end = tuple_list[index][1]

        elif current_end < tuple_list[index][1]:
            current_end = tuple_list[index][1]

    new_tuple: tuple[int, int] = (current_start, current_end)
    new_tuple_list.append(new_tuple)

    return new_tuple_list

print(merge_intervals([(1, 4), (2, 3), (5, 7)]))