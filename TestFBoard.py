import unittest
import FBoard
import config_TestFBoard


class TestFBoard(unittest.TestCase):
    def setUp(self):
        self.fb = FBoard.FBoard()

    def test_init(self):
        self.assertEqual(config_TestFBoard.fb_hard_coded_0, str(self.fb))

    def test_move_x_0(self):
        self.assertEqual(self.fb.move_x(1, 1), True)
        self.assertEqual(config_TestFBoard.fb_hard_coded_1, str(self.fb))

    def test_start_unfinished(self):
        self.assertEqual(self.fb.get_game_state(), "UNFINISHED")

    def test_x_win(self):
        for i, j in config_TestFBoard.x_moves_0:
            self.fb.move_x(i, j)
        for i, j, k, l in config_TestFBoard.o_moves_0:
            self.fb.move_o(i, j, k, l)
        for i, j in config_TestFBoard.x_moves_1:
            self.fb.move_x(i, j)
        self.assertEqual(self.fb.get_game_state(), "X_WON")

    def test_o_win(self):
        for i, j in config_TestFBoard.x_moves_0:
            self.fb.move_x(i, j)
        for i, j, k, l in config_TestFBoard.o_moves_1:
            self.fb.move_o(i, j, k, l)
        self.assertEqual(self.fb.get_game_state(), "O_WON")

    def test_invalid_x(self):
        self.assertEqual(self.fb.move_x(-1, -1), False)
        self.assertEqual(self.fb.move_x(0, 1), False)

    def test_invalid_o(self):
        self.assertEqual(self.fb.move_o(7, 7, 8, 8), False)
        print(self.fb)
        self.assertEqual(self.fb.move_o(6, 6, 5, 5), True)
        self.fb.move_o(5, 5, 4, 6)
        self.fb.move_o(4, 6, 3, 7)
        self.assertEqual(self.fb.move_o(3, 7, 2, 8), False)


if __name__ == "__main__":

    unittest.main()
