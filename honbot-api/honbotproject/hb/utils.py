from .models import PlayerMatchRNK, PlayerMatchCS, PlayerMatchACC


def pmoselect(mode):
    """
    returns the correct player match table based on mode
    """
    if mode == "rnk":
        return PlayerMatchRNK
    elif mode == "cs":
        return PlayerMatchCS
    elif mode == "acc":
        return PlayerMatchACC


def div(x, y):
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        return 0

def divmin(x, y):
    try:
        return (float(x) / (float(y) / 60))
    except ZeroDivisionError:
        return 0