"""Testing functions."""

__author__ = "730631751"

from ex05.dictionary import count
from ex05.dictionary import alphabetizer
from ex05.dictionary import invert
from ex05.dictionary import favorite_color
from ex05.dictionary import update_attendance


def test_count_use_1() -> None:
    """Primary use case."""
    assert count(["apples", "bananas", "apples"]) == {"apples": 2, "bananas": 1}


def test_count_use_2() -> None:
    """Secondary use case."""
    assert count(["oranges", "lemons", "grapefruits"]) == {
        "oranges": 1,
        "lemons": 1,
        "grapefruits": 1,
    }


def test_count_edge() -> None:
    """Testing an edge case."""
    assert count([]) == {}


def test_alphabetizer_use_1() -> None:
    """Primary use case."""
    assert alphabetizer(["apples", "bananas", "oranges"]) == {
        "a": ["apples"],
        "b": ["bananas"],
        "o": ["oranges"],
    }


def test_alphabetizer_use_2() -> None:
    """Secondary use case."""
    assert alphabetizer(["alligator", "armadillo"]) == {"a": ["alligator", "armadillo"]}


def test_alphabetizer_edge() -> None:
    """Testing an edge case."""
    assert alphabetizer([]) == {}


def test_invert_use_1() -> None:
    """Primary use case."""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_use_2() -> None:
    """Secondary use case."""
    assert invert({"forwards": "backwards"}) == {"backwards": "forwards"}


def test_invert_edge() -> None:
    """Testing an edge case."""
    assert invert({}) == {}


def test_favorite_color_use_1() -> None:
    """Primary use case."""
    assert favorite_color({"amy": "blue", "courtney": "blue"}) == "blue"


def test_favorite_color_use_2() -> None:
    """Secondary use case."""
    assert favorite_color({"jack": "yellow", "sam": "orange"}) == "yellow"


def test_favorite_color_edge() -> None:
    """Testing an edge case."""
    assert favorite_color({}) == ""


def test_update_attendance_use_1() -> None:
    """Primary use case."""
    sched: dict[str, list[str]] = {}
    update_attendance(sched, "Monday", "Emily")
    assert sched == {"Monday": ["Emily"]}


def test_update_attendance_use_2() -> None:
    """Secondary use case."""
    sched2: dict[str, list[str]] = {"Monday": ["Jessica", "Emily"]}
    update_attendance(sched2, "Tuesday", "Amanda")
    assert sched2 == {"Monday": ["Jessica", "Emily"], "Tuesday": ["Amanda"]}


def test_update_attendance_edge() -> None:
    """Testing an edge case."""
    sched3: dict[str, list[str]] = {"Monday": ["Jessica", "Emily"]}
    update_attendance(sched3, "Monday", "Emily")
    assert sched3 == {"Monday": ["Jessica", "Emily"]}
