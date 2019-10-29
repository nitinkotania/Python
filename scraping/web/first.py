


def print_dict(dict1):
	for k,v in dict1.items():
		if(isinstance(v,dict)):
			print_dict(v)
		else:
			print("{0}:{1}".format(k,v))

temp = {1:2, 3:4, 11:{5:6, 7:8}, 9:10}

print_dict(temp)



