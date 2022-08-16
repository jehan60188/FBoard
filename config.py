from enum import Enum


class STATES(Enum):
    UNFINISHED = 0
    O_WON = 1
    X_WON = 2


class PIPS(Enum):
    BLANK = "_"
    X = "x"
    O = "o"
