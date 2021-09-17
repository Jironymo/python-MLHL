from math import inf

def functionWithMaxValues(collection, *funcs_tuple):
    '''
    return a function with the highest sum over values.
    return the last in *functions_collection* if more than one is present 
    '''
    best_func_index = 0 
    max_sum = -inf
    for i, func in enumerate(funcs_tuple):
        temp_sum = sum((func(elem) for elem in collection))
        if temp_sum > max_sum:
            best_func_index = i
    return funcs_tuple[best_func_index]

print(functionWithMaxValues([1,2,3], lambda x: x**2, lambda x: x**3))


    
