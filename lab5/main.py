import numpy as np
import matplotlib.pyplot as plt


def task1():
    zeros = np.zeros(10)
    ones = np.ones(10)
    fives = np.full(10, 5.0)
    return zeros, ones, fives


def task2():
    x = np.random.rand(50)
    y = np.random.rand(50)
    sizes = np.random.rand(50) * 500
    plt.figure()
    plt.scatter(x, y, s=sizes)
    plt.savefig("scatter.png")
    plt.close()


def task3():
    return np.random.randint(30, 101, size=6)


def task4():
    x = np.arange(-5, 5, 0.1)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.title("y = sin(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("sin_plot.png")
    plt.close()


if __name__ == "__main__":
    # Task 1
    zeros, ones, fives = task1()
    print(zeros)   # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    print(ones)    # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    print(fives)   # [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

    # Task 2
    task2()        # saves scatter.png

    # Task 3
    print(task3()) # 6 random numbers between 30 and 100

    # Task 4
    task4()        # saves sin_plot.png
