import shelve
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

a_class_instance = a_class()

# Backup with shelve
bk = shelve.open('./backup_workspace/backup/backup_shelve', 'n')
for k in dir():
    try:
        bk[k] = globals()[k]
    except Exception:
        pass

import sys
print('Size of one item, e.g., `a_df`: ', sys.getsizeof(a_df))
print('Size of `bk`: ', sys.getsizeof(bk))

bk.close()


# ====== to load your session ======
import shelve

class a_class(object):
    def class_func(self, n):
        return n+1

def a_func(x):
    return x**2

bk_restore = shelve.open('./backup_workspace/backup/backup_shelve')
for k in bk_restore:
    globals()[k] = bk_restore[k]
bk_restore.close()

restored_variables = [el for el in dir() if el.startswith('a_')]
print(f'{len(restored_variables)} restored variables: ', restored_variables)
