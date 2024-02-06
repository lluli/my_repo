from lib.tracker import *
import pytest

def test_adding_a_track():
    music_tracker = MusicTracker()
    music_tracker.add('Farewell Transmission')
    assert music_tracker.listened_to == ['Farewell Transmission']

def test_adding_two_tracks():
    music_tracker = MusicTracker()
    music_tracker.add('Farewell Transmission')
    music_tracker.add('My Love Mine All Mine')
    assert music_tracker.listened_to == ['Farewell Transmission', 'My Love Mine All Mine']

def test_adding_three_tracks():
    music_tracker = MusicTracker()
    music_tracker.add('Farewell Transmission')
    music_tracker.add('My Love Mine All Mine')
    music_tracker.add('The Moon')
    assert music_tracker.listened_to == ['Farewell Transmission', 'My Love Mine All Mine', 'The Moon']

def test_see_three_tracks():
    music_tracker = MusicTracker()
    music_tracker.add('Farewell Transmission')
    music_tracker.add('My Love Mine All Mine')
    music_tracker.add('The Moon')
    result = print(music_tracker.listened_to)
    assert music_tracker.listened_to == ['Farewell Transmission', 'My Love Mine All Mine', 'The Moon']

def test_empty_string_added():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add('')
    result = str(e.value)
    assert result == "Please provide a track."