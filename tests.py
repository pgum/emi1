import unittest
import game

def test_czyIstniejeFunkcjaRzut():
    game.rzut()

def test_rzutNieWiekszyNiz6():
    assert(game.rzut() < 7)

