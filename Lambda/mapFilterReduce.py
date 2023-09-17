L = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x**2, L)))
#will check if x>4 in map and it will perform operation over every element, unlike filter
print(list(map(lambda x: x>4, L)))
#filter here will only add elements to the list which are more than 4
print(list(filter(lambda x: x>4, L)))