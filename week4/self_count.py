from typing import Any


class SelfCount:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def decrement_count(cls):
        cls.count -= 1
    

    def __init__(self):
        SelfCount.increment_count()

    def __getattribute__(self, name: str):
        if name == 'count':
            return SelfCount.count

    def __setattr__(self, name: str, value: Any) -> None:
        if name == 'count':
            return None

    def __delattr__(self, name: str) -> None:
        if name == 'count':
            return None

    def __del__(self):
        SelfCount.decrement_count()


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

