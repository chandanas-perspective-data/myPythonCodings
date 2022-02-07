
# Find the length of a segment

def line_length(dot1, dot2):
		[x1, y1], [x2, y2] = dot1, dot2
		return round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)


print (line_length([1,2], [2,4]))