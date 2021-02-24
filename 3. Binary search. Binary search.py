def binarySearch(array, target):
    return binarysearchhelper(array,target, 0, len(array)-1)
def binarysearchhelper(array, target, left, right):
	if left > right :
		return -1
	middle = (left + right)//2 
	potentialmatch = array [middle]
	if target == potentialmatch:
		return middle
	elif target < potentialmatch:
		return binarysearchhelper(array, target, left, middle-1)
	elif target > potentialmatch:
		return binarysearchhelper(array, target, middle+1, right)