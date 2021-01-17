import dill
import pandas

a_const = 1
a_lst = [1, 2, 3]
a_dict = {'a': 1, 'b': [1, 2]}
a_df = pandas.DataFrame({'col': [2, 4]})

a_lambda_func = lambda x: x**2

def a_func(x):
    return x**2

class a_class(object):
    def class_func(self, n):
        return n+1

class_instance = a_class()


# to save session
dill.dump_session('./backup_workspace/backup/backup_dill.db')


# ====== to load your session ======
import dill

bk_restore = dill.load_session('./backup_workspace/backup/backup_dill.db')

restored_variables = [el for el in dir() if el.startswith('a_')]
print(f'{len(restored_variables)} restored variables: ', restored_variables)
