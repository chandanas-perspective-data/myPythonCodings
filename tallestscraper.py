def tallest_skyscraper(lst):
	return sum(1 for i in lst if sum(i)>0)


print (tallest_skyscraper([[1,0, 1, 0], [1,0,0,0]]))