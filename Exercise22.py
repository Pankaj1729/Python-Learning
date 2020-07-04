#Order is: parameterised-->*args(act as tuple)-->default parameterised-->**kwargs(keyword argument(act as dictonary))

def kwargs_ex(reverse=False,**kwargs):
    if reverse:
        for k,v in kwargs.items():
            v=v[::-1]
            kwargs[k]=v.title()
        #kwargs={k:(v[::-1]).title() for k,v in kwargs.items()}
        return kwargs
    else:
        for k,v in kwargs.items():
            kwargs[k]=v.title()
        #kwargs={k:v.title() for k,v in kwargs.items()}    
        return kwargs

dict1={'Name':'pankaj','Name2':'priti'}
print(kwargs_ex(True**dict1))
