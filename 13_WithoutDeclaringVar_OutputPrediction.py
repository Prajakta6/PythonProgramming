def fun () :
    x = 10
    print (x)
    
fun()
print (x)


#Error - NameError: name 'x' is not defined
#Because x is defined inside the function which is inaccessible outside it.