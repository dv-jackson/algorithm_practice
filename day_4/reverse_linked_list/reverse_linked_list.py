def reverse_linked_list(given_list: list) -> list:
    return_list: list = []

    while len(given_list) != 0:
        return_list.append(given_list.pop())

    return return_list

print(reverse_linked_list([1,2,3,4,5]))

def reverse_in_space(given_list: list) -> list:
    head_pointer: int = 0
    tail_pointer: int = len(given_list) - 1

    flips: int = len(given_list) // 2

    counter: int = 0
    while counter < flips:
        temp_element = given_list[head_pointer]
        given_list[head_pointer] = given_list[tail_pointer]
        given_list[tail_pointer] = temp_element

        head_pointer += 1
        tail_pointer -=1
        counter += 1

    return given_list

print(reverse_in_space([2,2,3,4,5,2,1]))