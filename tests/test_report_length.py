from lib.report_length import * 

def test_report_length():
    result = report_length('the')
    assert result == 'This string was 3 characters long.'

def test_report_length():
    result = report_length('quick')
    assert result == 'This string was 5 characters long.'

def test_report_length():
    result = report_length('brown')
    assert result == 'This string was 5 characters long.'

def test_report_length():
    result = report_length('fox')
    assert result == 'This string was 3 characters long.'