import pickle
import pandas

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


# Backup with Pickle
def is_picklable(obj):
    try:
        pickle.dumps(obj)
    except Exception:
        return False
    return True


bk = {}
for k in dir():
    obj = globals()[k]
    if is_picklable(obj):
        try:
            bk.update({k: obj})
        except TypeError:
            pass


import sys
print('Size of one item, e.g., `a_df`: ', sys.getsizeof(a_df))
print('Size of `bk`: ', sys.getsizeof(bk))

# to save session
with open('./backup_workspace/backup/backup_pickle.pkl', 'wb') as f:
    pickle.dump(bk, f)

# to load your session
import pickle
with open('./backup_workspace/backup/backup_pickle.pkl', 'rb') as f:
    bk_restore = pickle.load(f)
