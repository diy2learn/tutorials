var1 = 1
var2 = [1, 2, 3]
print(dir())


print(globals()['var1'])
print(globals()['var2'])

import pickle
lambda_func = lambda x: x**2
pickle.dumps(lambda_func)

def is_picklable(obj):
    try:
        pickle.dumps(obj)
    except Exception:
        return False
    return True

lambda_func = lambda x: x**2
print('lambda_func: ', is_picklable(lambda_func))
print('var1: ', is_picklable(var1))