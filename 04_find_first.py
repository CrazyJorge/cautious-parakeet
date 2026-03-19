# 04_find_first.py
# Named Loop Pattern: FIND FIRST
#
# Walk the list. The MOMENT you find an element that matches,
# return it immediately.  Do not keep looking.
#
# This is the first pattern with an EARLY EXIT — the loop
# may not touch every element.  That's the whole point.
#
# If nothing matches, return a sentinel (None here).
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 04_find_first.py -v


def first_negative(lst):
    """Return the first negative integer, or None if there isn't one."""
    for item in lst:
        pass  # if item is negative, return it right now
    return None


def first_long(lst):
    """Return the first string longer than 4 characters, or None."""
    for word in lst:
        pass  # if word is long enough, return it right now
    return None


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_neg_basic():
    assert first_negative([3, 1, -4, 1, -5]) == -4

def test_neg_first_element():
    assert first_negative([-7, 2, 3]) == -7

def test_neg_none():
    assert first_negative([1, 2, 3]) is None

def test_neg_empty():
    assert first_negative([]) is None

def test_neg_all():
    assert first_negative([-1, -2, -3]) == -1

def test_long_basic():
    assert first_long(["hi", "cat", "tiger", "go"]) == "tiger"

def test_long_none():
    assert first_long(["hi", "cat", "go"]) is None

def test_long_empty():
    assert first_long([]) is None

def test_long_first():
    assert first_long(["whale", "a"]) == "whale"
