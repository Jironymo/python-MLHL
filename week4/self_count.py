from typing import Any

class SelfCount:
    _count = 0

    def __init__(self):
        SelfCount._count += 1

    @property
    def count(self):
        return SelfCount._count

    @count.setter
    def count(self, new_count):
        return None

    @count.deleter
    def count(self):
        return None

    def __del__(self):
        SelfCount._count -= 1


if __name__ == '__main__':
    a = SelfCount()
    b = SelfCount()
    c = SelfCount()
    a.count = 2
    del a.count

    print(a.count)
    print(b.count)
    print(c.count)

    del a
    print(c.count)

