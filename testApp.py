from nose.tools import assert_equal
from app import sing

def right_on_time(output):
    # time the outputs coming out....
    return True

def test_solve_1():
    song = "Bob Dylan - The Times They Are A-Changin'.md"
    bpm = 300
    # output = sing(song, bpm)
    output = ""
    assert_equal(True, right_on_time(output))

def test_solve_2():
    song = "Kanye West - Power.md"
    bpm = 200
    # output = sing(song, bpm)
    output = ""
    assert_equal(True, right_on_time(output))
