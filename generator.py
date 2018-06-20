

def my_gen():
    # Generator function:q contains yield statements
    yield n

# Using for loop

rag = input("enter the range\n")
freq = input("enter the freq\n")
for item in my_gen(1000,):
    print(item)    
