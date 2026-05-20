def add_two_numbers() -> int:
    user_input = input()

    new_list = user_input.split(",")

    value = 0

    for num in new_list:
        value += int(num)
    
    return value 



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
