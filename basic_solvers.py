import numpy as np
from numpy import ndarray


def missing_number(arr: ndarray):
    if len(np.where(arr == None)[0]) > 1:
        return None

    nums = np.zeros(9)
    for a in arr:
        if a is not None:
            np.put(nums, a-1, 1)

    missing_nums = np.where(nums == 0)

    return missing_nums[0][0]+1



test = np.array([5, 3, 2, 6, 1, 4, None, 9, 8])
#print(test)


print(missing_number(test))

