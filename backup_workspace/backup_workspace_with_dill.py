import dill

dill.dump_session('./your_bk_dill.pkl')
#to restore session:
dill.load_session('./your_bk_dill.pkl')