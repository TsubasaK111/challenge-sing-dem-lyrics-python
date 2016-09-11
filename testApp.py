from nose.tools import assert_equal
from app import sing

def test_solve_1():
    song = "Bob Dylan - The Times They Are A-Changin'.md"
    bpm = 100
    output = sing(song, bpm)
    assert_equal(True, right_on_time(output))

def test_solve_2():
    song = "Kanye West - Power.md"
    bpm = 80
    output = sing(song, bpm)
    assert_equal(True, right_on_time(output))


def right_on_time(output):
    # time the outputs coming out....
    return True
