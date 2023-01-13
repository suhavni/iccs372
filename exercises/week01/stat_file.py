import sys
import numpy as np

def get_float(string: str):
    try:
        return float(string)
    except ValueError:
        return None

def filter_none(iterable):
    return list(filter(lambda x: x is not None, iterable))

def print_summary(nums):
    print("mean: ", None if len(nums) == 0 else np.mean(nums), end=" ")
    print("std: ", None if len(nums) == 0 else np.std(nums), end=" ")
    print("min: ", None if len(nums) == 0 else np.min(nums), end=" ")
    print("max: ", None if len(nums) == 0 else np.max(nums))

def get_file_summary(file_name):
    try:
        f = open(file_name, "r")
        nums = np.array(filter_none([get_float(line) for line in f.readlines()]))
    except (IndexError, FileNotFoundError):
        nums = np.array([])
    finally:
        f.close()
    print_summary(nums)
    return nums

print("Statistics Summary")
total = [get_file_summary(file) for file in sys.argv[1:]]
print("combined:")
print_summary(np.concatenate(total))