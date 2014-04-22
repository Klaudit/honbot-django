from .models import (
    PlayerMatches, PlayerStats, PlayerStatsCasual, PlayerStatsPublic,
    PlayerMatchesCasual, PlayerMatchesPublic, HeroData
)


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


def psoselect(mode):
    """
    returns the correct player stat table based on mode
    """
    if mode == "rnk":
        return PlayerStats
    elif mode == "cs":
        return PlayerStatsCasual
    elif mode == "acc":
        return PlayerStatsPublic
