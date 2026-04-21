# Original problem with examples
# 📝 Problem: Given a string s containing only:
# '(', ')', '{', '}', '[', ']'
# Return True if the string is valid, otherwise False.
# ✅ Rules
# A string is valid if:
# Every opening bracket has a corresponding closing bracket
# Brackets close in the correct order
# Every closing bracket matches the most recent unmatched opening bracket
# 📥 Examples
# Input: "()"
# Output: True
# Input: "()[]{}"
# Output: True
# Input: "(]"
# Output: False
# Input: "([)]"
# Output: False
# Input: "{[]}"
# Output: True
# ⚠️ Edge Cases
# "" → True
# "(" → False
# ")" → False
# "(((" → False


# Restate the Problem:
# given a list of parentheses, make sure each parenthesis's closes properly

# Approach:
# - What data structure(s) am I using?
# - Stack
# - Hash Map

# - What algorithm/paradigm? (e.g., sliding window, DFS, BFS, binary search)
# - First in Last Out

# - Why this approach?
# Use the hashmap to get the open and closed matching parentheses
# Use the stack to tell which closed parentheses is valid to place

# Variables:
# - next_valid_close_stack: list[str]
# - parentheses_map: dict[str, str]

# Steps:
# - initialize parentheses_map
# - check if string empty
# - loop through list of parentheses
# - if the added parentheses is not in the keys of the parentheses_map (it is not an open parentheses)
#   - pop the next_valid_close_stack (if not empty) and compare the added parentheses to the next_valid
#       - if they are not equal, then return false
# - else (this means it is an open parentheses)
#   - add its key (the closed parentheses to the stack)
# - at the end, check if stack is empty
#   - if it is return true
#   - else return false

# Time Complexity:
# - O(n)

# Space Complexity:
# - O(n)


def valid_parentheses(parentheses: str) -> bool:
    parentheses_map: dict[str, str] = {"(": ")", "[": "]", "{": "}"}
    next_valid_close_stack: list[str] = []

    if len(parentheses) == 1:
        return False

    for parenth in parentheses:
        if parenth in parentheses_map:
            next_valid_close_stack.append(parentheses_map[parenth])

        else:
            if len(next_valid_close_stack) != 0:
                next_valid_close: str = next_valid_close_stack.pop()

                if parenth != next_valid_close:
                    return False

            else:
                return False

    return len(next_valid_close_stack) == 0

print(valid_parentheses(""))