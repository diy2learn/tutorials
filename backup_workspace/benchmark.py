import pandas
import backup_pickle

a_const = 1
a_lst = [1, 2, 3]
a_dict = {'a': 1, 'b': [1, 2]}
a_df = pandas.DataFrame({'col': [2, 4]})

lambda_func = lambda x: x**2

def a_func(x):
    return x**2

class a_class(object):
    def class_func(self, n):
        return n+1

class_instance = a_class()


backup_pickle.save_session()


