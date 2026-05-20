from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    name_age_dict = {}

    name_age_dict[name] = age

    return name_age_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    index_to_string_dict = {}

    for i in range(len(words)):
        index_to_string_dict[words[i]] = i
    
    return index_to_string_dict



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
