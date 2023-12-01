
def binary_search(value, lst):
	if len(lst) == 0:
		return False
	mid = len(lst)//2
	if value == lst[mid]:
		return mid
	elif value < lst[mid]:     #assume sorted like TA name said
		return binary_search(value, lst[:mid])
	else:
		return binary_search(value, lst[mid+1:]) + mid + 1

print(binary_search(5, [1,2,3,4,5,6,7,8,9,10]))
print(binary_search(7, [2,3,4,7,8]))