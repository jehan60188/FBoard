import config
from config import STATES, PIPS


class FBoard:
    def __init__(self, board_size=8, init_os=None, init_x=None):
        self.__board_size = board_size
        self.__board = [[PIPS.BLANK] * board_size for _ in range(board_size)]
        init_os = init_os if init_os is not None else [(5, 7), (6, 6), (7, 5), (7, 7)]
        for i, j in init_os:
            self.__board[i][j] = PIPS.O
        self.__state = STATES.UNFINISHED
        self.__occupied_x = init_x if init_x is not None else (0, 0)
        xi, xj = self.__occupied_x
        self.__board[xi][xj] = PIPS.X

    def get_game_state(self) -> str:
        return self.__state.name

    def move_x(self, tgt_i: int, tgt_j: int) -> bool:
        fromi, fromj = self.__occupied_x
        if not self.__is_allowed(fromi, fromj, tgt_i, tgt_j):
            return False
        curri, currj = self.__occupied_x
        self.__board[curri][currj] = PIPS.BLANK
        self.__board[tgt_i][tgt_j] = PIPS.X
        self.__occupied_x = (tgt_i, tgt_j)
        if tgt_i == tgt_j == self.__board_size - 1:
            self.__state = STATES.X_WON
        return True

    def move_o(self, curri: int, currj: int, tgt_i: int, tgt_j: int) -> bool:
        if not self.__is_allowed(curri, currj, tgt_i, tgt_j):
            return False
        if self.__board[curri][currj] != PIPS.O:
            return False
        if (
            tgt_i == curri + 1 and tgt_j == currj + 1
        ):  # row and col can't both increase:
            return False
        self.__board[curri][currj] = PIPS.BLANK
        self.__board[tgt_i][tgt_j] = PIPS.O
        if self.__xblocked():
            self.__state = STATES.O_WON
        return True

    def __xblocked(self):
        xi, xj = self.__occupied_x
        for step in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            xnew, ynew = xi + step[0], xj + step[1]
            if not self.__oob((xnew, ynew)) and self.__board[xnew][ynew] == PIPS.BLANK:
                return False
        return True

    def __oob(self, tgt):
        i, j = tgt
        if i < 0 or j < 0 or i >= self.__board_size or j >= self.__board_size:
            return True
        return False

    def __neighbors(self, i, j):
        results = set()
        for step in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            neighbor = (i + step[0], j + step[1])
            if not self.__oob(neighbor):
                results.add(neighbor)
        return results

    def __occupied(self, tgt):
        i, j = tgt
        return self.__board[i][j] != PIPS.BLANK

    def __is_allowed(self, fromi, fromj, toi, toj):
        if (
            self.__state != STATES.UNFINISHED
            or self.__oob((toi, toj))
            or self.__occupied((toi, toj))
        ):
            return False
        return (toi, toj) in self.__neighbors(fromi, fromj)

    def __str__(self):
        rr = ""
        for item in self.__board:
            rr = rr + ",".join([x.value for x in item]) + "\n"
        return rr
