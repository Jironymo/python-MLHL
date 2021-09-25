
def fixed_float(n=3):
    def decorator(func):
        from functools import wraps
        # use functools.wraps decorator to inherit attributes 
        # from the authentic *func*
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            pos_args = tuple(round(elem, n) if type(elem) == float else elem for elem in args)
            # too complex: name_args = {kwargs[key] : round(value, n) if type(value) == float else kwargs[key] : value for key, value in kwargs.items()}
            name_args = kwargs
            for key, value in kwargs.items():
                if type(value) == float: kwargs[key] = round(value, n) 

            result = func(*pos_args, **name_args)
            return round(result, n)
        return wrapper
    return decorator

if __name__ == '__main__':    
    @fixed_float(3)
    def sincos(a, b):
        from math import sin, cos
        result = sin(a) ** 2 + cos(b) ** 2
        return result

    @fixed_float(4)
    def aver(*args, sign=1):
        return sum(args) * sign

    from math import pi   
    print(sincos(pi / 2, pi / 2), sincos(pi / 4, 3 * pi / 4))
    print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))