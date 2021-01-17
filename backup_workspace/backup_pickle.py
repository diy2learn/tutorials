import pickle
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
        fpath = f'./data/backup_pickle.pkl'

    bk = {}
    for k in dir():
        obj = globals()[k]
        if is_picklable(obj):
            try:
                bk.update({k: obj})
            except TypeError:
                pass

    # to save session
    with open(fpath, 'wb') as f:
        pickle.dump(bk, f)
    logger.info(f"Pickled to {fpath}")


def load_session(
        fpath: str
):
    # to load your session
    with open(fpath, 'rb') as f:
        bk_restore = pickle.load(f)
    return bk_restore
