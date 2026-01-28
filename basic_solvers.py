import numpy as np
from numpy import ndarray


def missing_number(arr: ndarray) -> ndarray:
    if len(np.where(arr == None)[0]) != 1:
        return arr

    nums = np.zeros(9)
    idx = 0
    final_idx = None
    for a in arr:
        if a is not None:
            np.put(nums, a-1, 1)
        else:
            final_idx = idx
        idx += 1


    print(final_idx)
    missing_nums = np.where(nums == 0)
    print(missing_nums)

    np.put(arr, final_idx, int(missing_nums[0][0]+1))
    return arr



test = np.array([5, 3, 2, 6, 1, 7, None, 9, 8])
#print(test)

print(missing_number(test))

