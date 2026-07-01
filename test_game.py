import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

def test_exception_whel_input_is_gone(game):
    with pytest.raises(TypeError):
        game.guess(None)