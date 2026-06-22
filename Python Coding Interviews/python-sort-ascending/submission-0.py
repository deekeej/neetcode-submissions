from typing import List


def sort_words(words: List[str]) -> List[str]:
    copyarr=list(words)
    n = len (copyarr)
    for z in range (n):
        for j in range (n-z-1):
            if copyarr[j] > copyarr[j+1]:
                copyarr[j],copyarr[j+1] = copyarr[j+1],copyarr[j]
    return copyarr


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return sorted(numbers)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
