

""" decorator package """

class validate_decorator():
    pass

""" Decorator: To add the validation code for provided parameteres """ 
def Validate_input(original_function):
     def new_function(*args,**kwargs):
          for value in args[1:]:
              if(value < 0):
                  print("************************************************")
                  print("Provided input is non-positive value")
                  return False
          x = original_function(*args,**kwargs)                
          return x                                             
     return new_function 


















