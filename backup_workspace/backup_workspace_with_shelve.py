import shelve

bk = shelve.open('./your_bk_shelve.pkl','n')
for k in dir():
    try:
        bk[k] = globals()[k]
    except Exception:
        pass
bk.close()

# to restore
bk_restore = shelve.open('./your_bk_shelve.pkl')
for k in bk_restore:
    globals()[k] = bk_restore[k]
bk_restore.close()
