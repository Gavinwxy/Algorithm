def mergeCntSplitInv(left, right):
	i, j = 0, 0
	splitInv = 0
	sortedArray = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			sortedArray.append(left[i])
			i += 1
		else:
			sortedArray.append(right[j])
			j += 1
			splitInv += len(left)-i
	sortedArray += left[i:]
	sortedArray += right[j:]
	return splitInv, sortedArray 



def sortCntInv(inputArray):
	'''This function is based on mergersort to implement inversion count
	Args: 
		inputArray (list): unsorted array
	Returns:
		invs (int): number of inversions
		sortedArray (list): sorted array 
	''' 
	n = len(inputArray)
	if n <= 1:
		return 0, inputArray
	else:
		midIdx = int(n/2)
		leftInv, left = sortCntInv(inputArray[:midIdx])
		rightInv, right = sortCntInv(inputArray[midIdx:])
		splitInv, sortedArray = mergeCntSplitInv(left, right)
		invs = leftInv+rightInv+splitInv
		return invs, sortedArray


if __name__ == '__main__':
	file = open("IntegerArray.txt","r") 
	inputArray = []
	for line in file:
		inputArray.append(int(line)) # Note that default format by reading is string
	file.close()
	#inputArray = [10,9,8,7,6,5,4,3,2,1]
	#inputArray = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
	#print(inputArray)
	invs, sortedArray = sortCntInv(inputArray)
	print(invs)