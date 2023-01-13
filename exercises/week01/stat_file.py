import sys
import numpy as np

def get_float(string: str):
    try:
        return float(string)
    except ValueError:
        return None

def filter_none(iterable):
    return list(filter(lambda x: x is not None, iterable))

try:
    file = sys.argv[1]
    f = open(file, "r")
    nums = np.array(filter_none([get_float(line) for line in f.readlines()]))
except (IndexError, FileNotFoundError):
    nums = np.array([])

print("mean: ", None if len(nums) == 0 else np.mean(nums))
print("std: ", None if len(nums) == 0 else np.std(nums))
print("min: ", None if len(nums) == 0 else np.min(nums))
print("max: ", None if len(nums) == 0 else np.max(nums))