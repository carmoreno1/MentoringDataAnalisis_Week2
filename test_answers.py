from unittest import mock
from answers import Exercises

exercises = Exercises()

# Test for Drive
@mock.patch("builtins.input")
def test_is_able_to_drive(input_mock, capsys):
    input_mock.return_value = 18
    exercises.is_able_to_drive()
    output = capsys.readouterr()
    assert 'is allowed to drive' in output.out

@mock.patch("builtins.input")
def test_is_NOT_able_to_drive(input_mock, capsys):
    input_mock.return_value = 10
    exercises.is_able_to_drive()
    output = capsys.readouterr()
    assert 'is not allowed to drive' in output.out

@mock.patch("builtins.input")
def test_error_input_age(input_mock, capsys):
    input_mock.return_value = 'ABC'
    exercises.is_able_to_drive()
    output = capsys.readouterr()
    assert 'An error has happened' in output.out

# Test for Colors

@mock.patch("builtins.input")
def test_exit(input_mock, capsys):
    input_mock.return_value ='quit'
    exercises.check_color()
    output = capsys.readouterr()
    assert 'bye' in output.out

@mock.patch("builtins.input")
def test_error(input_mock, capsys):
    input_mock.side_effect = Exception("An error has happened")
    exercises.check_color()
    output = capsys.readouterr()
    assert 'An error has happened' in output.out


def get_print():
    print("blue")
    return Exception('********')

@mock.patch("builtins.print")
@mock.patch("builtins.input")
def test_color(input_mock, print_mock, capsys):
    input_mock.return_value = 'blue'
    print_mock.side_effect = get_print()
    exercises.check_color()
    output = capsys.readouterr()
    print('***********************>>>',output)
    assert 'blue' in print_mock.out