def flatten(lst):
	stack = []
	for e in lst:
		if type(e) == list:
			stack.extend(flatten(e))
		else:
			stack.append(e)
	return stack

l = [1, 2, [3, 4, [5]]]
print(flatten(l))
