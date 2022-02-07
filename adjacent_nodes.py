def is_adjacent(matrix, node1, node2):
	return bool(matrix[node1][node2])

print (is_adjacent([
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
], 0, 1))