# Original problem with examples
# 📝 Problem: Two Sum
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
#
# You may assume exactly one solution exists
# You may not use the same element twice
#
# Return the answer in any order
#
# 📥 Example 1
# Input:
# nums = [2, 7, 11, 15]
# target = 9
#
# Output:
# [0, 1]
# 📥 Example 2
# Input:
# nums = [3, 2, 4]
# target = 6
#
# Output:
# [1, 2]
# 📥 Example 3
# Input:
# nums = [3, 3]
# target = 6
#
# Output:
# [0, 1]
# ⚠️ Requirements
# Aim for better than O(n²) (brute force is NOT acceptable for interviews)
# This problem tests:
# Hash maps (dictionaries in Python)
# Time optimization mindset


# ----------------------------------------------------------------------------------------
# Problem:
# Given a list of numbers and a target,
# list the indices of the numbers whose sum adds up to the target
# The same elements cannot be used twice
# There will always be one solution (make a Variant to make it so that there may be no solution)
# Return answer in any order

# Approach:
# - What data structure(s) am I using?
# For this it is advised to use Hash Maps

# - What algorithm/paradigm? : Hash Map Lookup
# - Why this approach?:
# I can iterate through each number (subtract it from the target) and see if that
# result exists in the hash map

# Variables:
# - num_list list[int], num_map Dict [int, int], int target, int index, int num_needed, is_found bool

# Steps:
# Prompt user for list of integers
# Store as list of ints
# check if list is empty (exit if is)

# Prompt user for target
# store as int

# use for loop to inex through each element in num_list
# subtract the element from the target
# check if num_needed is in the nums_map

# if it is, then set is_found to true and break the loop
# else add element to nums_map with index

# check is_found bool
# if found print indexes
# else return not found message

# Time Complexity:
# - O(n)

# Space Complexity:
# - O(n) since the array is size of n

def two_sum(nums: list[int], target: int) -> list[int]:
    index: int = 0
    num_needed: int

    num_map: dict[int, int] = {}

    for num in nums:
        num_needed = target - num

        if num_needed in num_map:
            return [num_map[num_needed], index]

        else:
            num_map[num] = index

        index += 1

    return [-1]