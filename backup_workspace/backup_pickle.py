import pickle
import os
from datetime import datetime
import logging


logger = logging.getLogger(__name__)


def is_picklable(obj):
    try:
        pickle.dumps(obj)
    except Exception:
        return False
    return True


def get_timestamp():
    """
    Examples
    --------
    >>> print(get_timestamp())
    20210117T124929
    """
    return datetime.now().strftime("%Y%m%dT%H%M%S")


def save_session(
        fpath: str = None):
    if fpath is None:
        if not os.path.exists('./backup'):
            os.makedirs('./backup')
        fpath = f'./backup/backup_pickle.pkl'

    __bk = {}
    black_list = ['__bk']
    keys = list(set(list(globals().keys())) - set(black_list))
    for k in keys:
        print('k: ', k)
        obj = globals()[k]
        if is_picklable(obj):
            try:
                __bk.update({k: obj})
            except TypeError:
                pass

    # to save session
    with open(fpath, 'wb') as f:
        pickle.dump(__bk, f)
    logger.info(f"Pickled to {fpath}")


def load_session(
        fpath: str = None
):
    if fpath is None:
        fpath = f'./backup/backup_pickle.pkl'
    # to load your session
    with open(fpath, 'rb') as f:
        bk_restore = pickle.load(f)
    return bk_restore



