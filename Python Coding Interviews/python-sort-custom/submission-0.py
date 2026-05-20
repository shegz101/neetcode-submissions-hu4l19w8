from typing import List

# Helper function
def sort_word_by_len(word: str):
    return len(word)

def sort_num_by_abs(num):
    return abs(num)

def sort_words(words: List[str]) -> List[str]:    
    words.sort(key=sort_word_by_len, reverse=True)

    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=sort_num_by_abs)

    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
