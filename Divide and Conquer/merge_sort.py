
def merge(leftArray, rightArray):
	''' This function is an implementation of merging two sorted arrays.
		It is the most important operation in the merge sort algorithm

	Args: 
		leftArray (list): the first sorted array
		rightArray (list): the second sorted array
	Returns:
		result (list): the combined version of sorted array 
	'''

	i, j = 0, 0
	result = []
	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] < rightArray[j]:
			result.append(leftArray[i])
			i += 1
		else:
			result.append(rightArray[j])
			j += 1
	result += leftArray[i:]
	result += rightArray[j:]
	return result


def mergeSort(inputArray):
	'''This is the main function fo merge sort algorithm applying recusion method
	Args: 
		inputArray (list): unsorted array
	Returns:
		inputArray (int): single value list, which is the base case
		merge(leftArray, rightArray) (list): sorted and combiend version of an array called recursively
	'''
	n = len(inputArray)
	if n <= 1:
		return inputArray
	else:
		midIdx = int(n/2)
		leftArray = mergeSort(inputArray[:midIdx])
		rightArray = mergeSort(inputArray[midIdx:])
		return merge(leftArray, rightArray)


if __name__ == '__main__':
	a = [5,3,1]
	b = [2,4,6]
	print(mergeSort(a+b))

