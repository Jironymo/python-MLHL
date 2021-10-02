def sizer(cls):

    class Wrapper:

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            
            try:
                self.size = len(self._obj)
            except TypeError:
                self.size = abs(int(self._obj))

        def __repr__(self):
            return str(self._obj) 

    return Wrapper

if __name__ == '__main__':
    @sizer
    class S(str): pass

    @sizer
    class N(float): pass

    s = S("QSXWDC")
    n = N(2.718281828459045)
    print(s, n)
    print(s.size, n.size)
    s.size, n.size = "Wait", "what?"
    print(s.size, n.size) 