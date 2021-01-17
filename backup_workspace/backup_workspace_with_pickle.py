import pickle


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

# to save session
with open('./your_bk.pkl', 'wb') as f:
    pickle.dump(bk, f)

# to load your session

with open('./your_bk.pkl', 'rb') as f:
    bk_restore = pickle.load(f)