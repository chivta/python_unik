import random


def task1(x, a, b):
    if a > b:
        a, b = b, a
    return [random.randint(a, b) for _ in range(x)]


def task2(lst):
    return [x for x in lst if x > 0]


def task3(lst):
    return {i: v for i, v in enumerate(lst)}


def task4(lst):
    return {x ** 2 for x in lst}


def task5(n):
    a, b = 1, 1
    for _ in range(n):
        print("here")
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # Task 1
    print(task1(5, 1, 10))    # [3, 7, 1, 9, 4]
    print(task1(3, 5, 5))     # [5, 5, 5]

    # Task 2
    print(task2([-3, 0, 5, -1, 7, 2, -9, 4]))  # [5, 7, 2, 4]
    print(task2([-1, -2, -3]))                  # []

    # Task 3
    print(task3(["alpha", "beta", "gamma"]))    # {0: 'alpha', 1: 'beta', 2: 'gamma'}
    print(task3([]))                            # {}

    # Task 4
    print(task4([1.3, 2.5, 3.1]))  # {1.6900000000000002, 6.25, 9.610000000000001}
    print(task4([2, 3]))           # {4, 9}

    # Task 5
    print(list(task5(10)))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    print(list(task5(1)))   # [1]

    for x in task5(10):
        print("there")
