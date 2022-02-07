def area_of_country(name, area):
    return "{} is {:.2%} of the total world's landmass".format(name, area / 148940000)


print (area_of_country("Australia", 17098242))





l = [1,3,3,3,2,5,2,6,7,3]
print ({each:l.count(each) for each in l})