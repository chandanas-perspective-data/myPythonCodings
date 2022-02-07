def insertion_sort(GivenList):
	for i in range(1, len(GivenList)):
		curNum = GivenList[i]
		for j in range(len(GivenList)-1, 0, -1):
			if GivenList[j] > curNum:
				GivenList[j+1] = GivenList[j]
			else:
				GivenList[j+1] = curNum
				break


list = [6,3,2,7,9,1]
insertion_sort(list)

print (list)