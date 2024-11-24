""" Modify all your previous function to print your execution time """

import time as t

from dev import devide as dv1
from functionScope import outer_function as dv2
from immut import modifu_mutable as dv4
from immut import modify_immutable as dv3


def time_execution(func, *args, **kwargs):
    start_time = t.time()
    result = func(*args, **kwargs)
    end_time = t.time()
    execution_time = end_time - start_time
    print(f"Time of execution {func.__name__}: is {execution_time:.6f} seconds")
    return result


time_execution(dv1, 6, 5)
time_execution(dv2)
time_execution(dv3, 6)
time_execution(dv4, [1, 2, 3])
