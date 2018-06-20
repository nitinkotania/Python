

#print a nested disctionary 

def dict_print(dict1):
	for k,v in dict1.items():
		if isinstance(v,dict):
			dict_print(v)
		else:
			print("{0} : {1}".format(k,v))



d = {1:2, 3:4, 5:{23:34, 45:56}, 7:8}

dict_print(d)
