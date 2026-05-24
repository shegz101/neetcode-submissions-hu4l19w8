from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score = float('-inf')

    i = 0

    while i < len(scores):
        for name, score in scores:
           highest_score = max(highest_score, score)

        for name, score in scores:
            if highest_score == score:
                return name 




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
