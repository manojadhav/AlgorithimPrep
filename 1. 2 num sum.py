{"array": [3, 5, -4, 8, 11, 1, -1, 6], "targetSum": 10}


def twonumbersum (array, targetsum)
    for i in range(len(array -1)):
        fn = array[i]
        for j in range(i+1, len(array)):
            sn = array[j]
            if fn + sn == targetsum:
                return [fn, sn]
    return []


def twonumbersum (array, targetsum)
    nums = {}
    pm = tragetsum - num
    if pm in nums:
        return [pm, num]
    else:
        nums{num} = True
    return []



def twonumbersum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right :
        currentsum = array[left] + array[right]
        if targetSum == currentsum:
            return [array[left], array[right]]
        elif currentsum > targetSum:
            right -= 1
        elif currentsum < targetSum:
            left += 1
        return []