
import pytest
from project import room_handler, text_wrapper, reset


@pytest.mark.parametrize("direction, starting_room, end_room", [
    ("north", 250, 350),
    ("east", 350, 351),
    ("west", 351, 350),
    ("south", 350, 250)
])

def test_room_handler(direction, starting_room, end_room):
    assert room_handler(direction, starting_room) == end_room


def test_text_wrapper():
    assert len(text_wrapper("1234")) == 4
    assert len(text_wrapper("The quick brown fox jumps over the lazy dogs")) == 44


def test_reset(mocker):
    mock_player = mocker.patch('project.player')
    reset()
    assert mock_player.phone_charged == False
    assert mock_player.phone_updated == False
    assert mock_player.phone_signal == False
    assert mock_player.current_room == 250

