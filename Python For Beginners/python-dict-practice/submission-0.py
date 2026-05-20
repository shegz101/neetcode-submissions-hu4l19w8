from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_dict = {}

    for ch in word:
        count_dict[ch] = count_dict.get(ch, 0) + 1
    
    return count_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
