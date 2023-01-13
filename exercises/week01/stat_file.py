import sys
import numpy as np

def get_float(string: str):
    try:
        return float(string)
    except ValueError:
        return None

def filter_none(iterable):
    return list(filter(lambda x: x is not None, iterable))

file = sys.argv[1]
f = open(file, "r")
nums = np.array(filter_none([get_float(line) for line in f.readlines()]))

print("mean: ", np.mean(nums))
print("std: ", np.std(nums))
print("min: ", np.min(nums))
print("max: ", np.max(nums))