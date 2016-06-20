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

class TestRunda(unittest.TestCase):

    def test_rundaMaDacPareWynikow(self):
        wyn_czlo, wyn_cpu= game.runda()
        self.assertTrue(wyn_czlo > 1)
        self.assertTrue(wyn_czlo < 13)
        self.assertTrue(wyn_cpu > 1)
        self.assertTrue(wyn_cpu < 13)


if __name__ == '__main__':
    unittest.main()
