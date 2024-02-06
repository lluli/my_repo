from lib.diary import DiaryEntry
import pytest

def test_format_of_diary():
    diary_entry = DiaryEntry('Ledias Diary', 'Hello and welcome to my diary, today I ate a really really really good strawberry.')
    result = diary_entry.format()
    assert result == 'Ledias Diary: Hello and welcome to my diary, today I ate a really really really good strawberry.'

def test_count_word_in_diary_entry():
    diary_entry = DiaryEntry('Ledias Diary', 'Hello and welcome to my diary, today I ate a really really really good strawberry.')
    result = diary_entry.count_words()
    assert result == 15 

def test_reading_time_for_a_diary_entry():
    diary_entry = DiaryEntry('Ledias Diary', 'Hello and welcome to my diary, today I ate a really really really good strawberry.')
    result = diary_entry.reading_time(5)
    assert result == 3

def test_reading_time_for_a_diary_entry():
    diary_entry = DiaryEntry('Ledias Diary', 'Hello and welcome to my diary, today I ate a really really really good strawberry.')
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    result = str(e.value)
    assert result == 'Please learn to read first!'

def test_reading_chunk_of_diary():
    diary_entry = DiaryEntry('Ledias Diary', 'Hello and welcome to my diary today I ate a really really really good strawberry.')
    assert diary_entry.reading_chunk(5,1) == 'Hello and welcome to my'
    assert diary_entry.reading_chunk(5,1) == 'diary today I ate a'
    assert diary_entry.reading_chunk(5,1) == 'really really really good strawberry.'