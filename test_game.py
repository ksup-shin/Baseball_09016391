import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

def test_exception_whel_input_is_gone(game):
    with pytest.raises(TypeError):
        game.guess(None)

def test_execption_when_input_length_is_unmatched(game):
    with pytest.raises(TypeError):
        game.guess("12")