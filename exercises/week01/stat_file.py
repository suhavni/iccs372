import sys
import numpy as np

def get_float(string: str):
    try:
        return float(string)
    except ValueError:
        return None

def filter_none(iterable):
    return list(filter(lambda x: x is not None, iterable))

def run_function(f, nums):
    return None if len(nums) == 0 else f(nums)

def print_summary(nums):
    print("mean: ", run_function(np.mean, nums), end=" ")
    print("std: ", run_function(np.std, nums), end=" ")
    print("min: ", run_function(np.min, nums), end=" ")
    print("max: ", run_function(np.max, nums), end=" ")
    print("n: ", len(nums))

def get_file_summary(file_name):
    try:
        f = open(file_name, "r")
        nums = np.array(filter_none([get_float(line) for line in f.readlines()]))
    except (IndexError, FileNotFoundError):
        nums = np.array([])
    finally:
        f.close()
    print(file_name)
    print_summary(nums)
    return nums

print("Statistics Summary")
total = [get_file_summary(file) for file in sys.argv[1:]]
print("combined:")
print_summary(np.concatenate(total))