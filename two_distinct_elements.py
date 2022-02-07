
# Return two distinct elements of a list
def return_unique(lst):
  return [i for i in lst if lst.count(i)==1]


print (return_unique([1,3,3,1,2,5,6,8,6,5]))