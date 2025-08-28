import m3_1
import pytest

def test_compare_with_five_smaller(monkeypatch, capsys):

    user_input = "4"
    expected_output = "The number is smaller than 5"

    monkeypatch.setattr("builtins.input", lambda _: user_input)
    m3_1.compare_with_five()
    captured = capsys.readouterr()

    assert expected_output in captured.out


def test_compare_with_five_greater(monkeypatch, capsys):
    # Phase 1: Test Case
    user_input = "7"
    expected_output = "The number is greater than 5"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    m3_1.compare_with_five()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out

