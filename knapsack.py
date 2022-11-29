sacks = 3


k = sacks
source = [1, 2, 3, 4, 5, 6, 7]

source.sort(reverse = True)
def genArrays(count):
	buffer = []
	for i in range(count):
		buffer.append([])
	return buffer
tuples = ([[[x]] + genArrays(k-1) for x in source])

while(len(tuples) > 1):
	sumDifA = -1; aIndex = None
	sumDifB = -1; bIndex = None

	for i in range(len(tuples)):
		minVal = 99999
		maxVal = -1

		for j in range(k):
			buffer = sum(tuples[i][j])
			if buffer < minVal:
				minVal = buffer
			if buffer > maxVal:
				maxVal = buffer

		sumDif = maxVal - minVal
		if sumDif > sumDifA: 
			sumDifB = sumDifA; bIndex = aIndex
			sumDifA = sumDif; aIndex = i
		elif sumDif > sumDifB:
			sumDifB = sumDif; bIndex = i

	for i in range(k):
		tuples[aIndex][i].extend(tuples[bIndex][-1-i])

	tuples[aIndex].sort(reverse = True, key = lambda x: sum(x))
	tuples.pop(bIndex)

result = tuples[0]

print(len(result), 'sacks:')
print(result)
