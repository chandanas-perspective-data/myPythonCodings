# Converting list into a Ditionary
# Take two separate lists with elements
list1=['apple','banana','cherry','grapes']
list2=['red','yellow','pink','green']

x=zip(list1,list2) # make a dictionary
y=dict(x)       # display key- value pairs from dictionary y
for i in y:
	print("{:15s}----{:15s}".format(i,y[i]))
