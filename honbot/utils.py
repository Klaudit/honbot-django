from .models import PlayerMatches, PlayerMatchesCasual, PlayerMatchesPublic


def pmoselect(mode):
    """
    returns the correct player match table based on mode
    """
    if mode == "rnk":
        return PlayerMatches
    elif mode == "cs":
        return PlayerMatchesCasual
    elif mode == "acc":
        return PlayerMatchesPublic
