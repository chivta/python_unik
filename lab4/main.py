import sqlite3
from typing import get_type_hints


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class ORMMapper:
    _type_map = {str: "TEXT", int: "INTEGER", float: "REAL"}

    def __init__(self, cls):
        self._cls = cls

    def convert_to_db(self):
        hints = get_type_hints(self._cls)
        if not hints:
            hints = {
                k: type(v)
                for k, v in vars(self._cls).items()
                if not k.startswith("_") and not callable(v)
            }
        columns = ", ".join(
            f"{name} {self._type_map.get(typ, 'TEXT')}"
            for name, typ in hints.items()
        )
        sql = f"CREATE TABLE {self._cls.__name__} ({columns});"
        print(sql)
        conn = sqlite3.connect(":memory:")
        conn.execute(sql)
        conn.commit()
        conn.close()


class StringHolder:
    def __init__(self):
        self._string = ""

    def get_string(self, s):
        self._string = s

    def print_upper_string(self):
        result = ""
        for x in self._string:
            if 'a' <= x <= 'z':
                x = chr(ord(x) - 32)
            result += x
        print(result)


class Counter:
    def __init__(self, *, start=0, lower=0, upper=9):
        self._apply(start=start, lower=lower, upper=upper)

    def reinitialize(self, *, start, lower, upper):
        self._apply(start=start, lower=lower, upper=upper)

    def increment(self):
        if self.value >= self.upper:
            raise ValueError(f"Upper bound {self.upper} reached")
        self.value += 1

    def decrement(self):
        if self.value <= self.lower:
            raise ValueError(f"Lower bound {self.lower} reached")
        self.value -= 1

    def _apply(self, *, start, lower, upper):
        if lower > upper:
            raise ValueError("lower must be <= upper")
        if not (lower <= start <= upper):
            raise ValueError("start must be within [lower, upper]")
        self.value = start
        self.lower = lower
        self.upper = upper


if __name__ == "__main__":
    # Task 1
    s1 = Singleton()
    s2 = Singleton()

    # "is" checks if both variables point to the same object in memory
    print(s1 is s2)    # True


    # Task 2
    class Person:
        name: str
        age: int
        height: float

    mapper = ORMMapper(Person)
    mapper.convert_to_db()    
    # will print: CREATE TABLE Person (name TEXT, age INTEGER, height REAL);


    # Task 3
    holder = StringHolder()
    holder.get_string("hello world")
    holder.print_upper_string()    # HELLO WORLD


    # Task 4
    counter = Counter()
    print(f"value={counter.value}, lower={counter.lower}, upper={counter.upper}")    # value=0, lower=0, upper=9

    steps = []
    for _ in range(15):
        try:
            counter.increment()
            steps.append(counter.value)
        except ValueError:
            break
    print(steps)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    counter.reinitialize(start=5, lower=-3, upper=10)
    print(f"value={counter.value}, lower={counter.lower}, upper={counter.upper}")    # value=5, lower=-3, upper=10

    steps = []
    for _ in range(15):
        try:
            counter.decrement()
            steps.append(counter.value)
        except ValueError:
            break
    print(steps)    # [4, 3, 2, 1, 0, -1, -2, -3]
