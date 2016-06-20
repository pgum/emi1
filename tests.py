import unittest
import game

class TestRzutyKostka(unittest.TestCase):

    #pierwszy test poprawiony i przechodzi!
    def test_rzutNieWiekszyNiz6(self):
        self.assertLess(game.rzut(), 7)

    #teraz przechodzi
    def test_rzutNieMniejszyNiz1(self):
        self.assertGreater(game.rzut(), 0)
    #po tych dwoch testach wiemy ze pojedynczy rzut koscia nie daje debilnych wynikow typu -1

if __name__ == '__main__':
    unittest.main()
