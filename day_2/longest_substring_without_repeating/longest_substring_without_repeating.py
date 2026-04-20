# Original problem with examples
# 🧠 Problem: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# 📥 Example 1
# Input: s = "abcabcbb"
# Output: 3
# Explanation: "abc"
# 📥 Example 2
# Input: s = "bbbbb"
# Output: 1
# Explanation: "b"
# 📥 Example 3
# Input: s = "pwwkew"
# Output: 3
# Explanation: "wke"
# ⚠️ Requirements
# Target: O(n) time
# Pattern: Sliding Window + Hash Set/Map
# Must handle:
# Empty string
# All same characters
# All unique characters

# Restate the Problem:
# Given a string of characters, find the long substring that doesn't have repeating characters

# Approach:
# - What data structure(s) am I using?:
# - hashmap

# - What algorithm/paradigm?:
# - Sliding Window

# - Why this approach?
# - Loop through the string one time and keep adding to the hashmap
# - the character in the hashmap exists then mark the max and clear the hashmap and keep going

# Variables:
# - char_hashmap: dict[str, int]
# - max_window: int
# - left_index: int
# - right_index: int

# Steps:
# - Define the empty char_hashmap
# - loop through the string
# - check if the character is in the hashmap
# - if it is
#   - set lef_index to the max index value of the str key in char_hashmap + 1 or left_index + 1
# - check window (right_index - left_index + 1) for max_window
# - add character to the hashmap with the right_index as the value

# Time Complexity:
# - O(n)

# Space Complexity:
# - O(n)

def longest_substring(string: str) -> int:
    char_hashmap: dict[str, int] = {}
    max_window: int = 0
    left_index: int = 0
    right_index:int = 0

    for character in string:
        if character in char_hashmap:
            left_index = max(left_index, char_hashmap[character] + 1)

        max_window = max(max_window, right_index - left_index + 1)
        char_hashmap[character] = right_index

        right_index += 1


    return max_window

print(longest_substring("tmmzuxt"))
print(longest_substring("pekvezxtkpp"))