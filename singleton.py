
class singleton():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not singleton._instance:
            print("creating instance of class")
            singleton._instance = object.__new__(cls, *args, **kwargs)
        else:
            print("returning already created object")
        return singleton._instance


a = singleton()
b = singleton()
c = singleton()
d = singleton()
e = singleton()
f = singleton()

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

 
