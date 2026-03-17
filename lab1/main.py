from collections import Counter


def task1(list1: list, list2: list) -> bool:
    return list1[0] == list2[0] or list1[-1] == list2[-1]


def task2(lst: list) -> dict:
    return dict(Counter(lst))


def task3(lst: list) -> None:
    print(*lst, sep='; ')


def task4(lst: list) -> list[list]:
    return [list(range(n + 1)) for n in lst]


def task5(dicts: list[dict]) -> dict:
    result = {}
    for d in dicts:
        for k, v in d.items():
            result.setdefault(k, []).append(v)
    return result


if __name__ == '__main__':
    # Task 1
    print(task1([1, 2, 3], [3, 4, 5]))   # False
    print(task1([1, 2, 3], [4, 5, 6]))   # False
    print(task1([1], [1]))               # True  

    # Task 2
    print(task2([1, 2, 2, 3]))            # {1: 1, 2: 2, 3: 1}
    print(task2([]))                      # {}

    # Task 3
    task3([1, 'a', True])                 # 1; a; True

    # Task 4
    print(task4([1, 2, 3]))              # [[0, 1], [0, 1, 2], [0, 1, 2, 3]]
    print(task4([0]))                    # [[0]]

    # Task 5
    print(task5([{'a': 1, 'b': 2}, {'a': 3, 'c': 4}]))  # {'a': [1, 3], 'b': [2], 'c': [4]}
    print(task5([]))                                      # {}
