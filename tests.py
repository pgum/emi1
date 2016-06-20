import unittest
import game

class TestRzutyKostka(unittest.TestCase):

    def test_rzutNieWiekszyNiz6(self):
        self.assertLess(7, game.rzut())

if __name__ == '__main__':
    unittest.main()
