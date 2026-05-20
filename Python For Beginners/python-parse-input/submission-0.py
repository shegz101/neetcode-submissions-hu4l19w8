from typing import List

def read_integers() -> List[int]:
    user_input = input()

    user_input_list = user_input.split(",")

    int_list = []

    for string in user_input_list:
        int_list.append(int(string))

    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
