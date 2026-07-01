import pytest
from game import Game


def test_exception_whel_input_is_gone():
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)