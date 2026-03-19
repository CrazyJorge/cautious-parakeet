# 02_count.py
# Named Loop Pattern: COUNT
#
# Walk the whole list. Every time an element meets the condition,
# add 1 to a counter. Return the count at the end.
#
# The counter starts at 0.  The loop body is: test, then increment.
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 02_count.py -v


def count_positive(lst):
    """Return how many integers in lst are greater than zero."""
    count = 0
    for item in lst:
        pass  # if item is positive, increment count
    return count


def count_short(lst):
    """Return how many strings in lst have length <= 3."""
    count = 0
    for word in lst:
        pass  # if word is short enough, increment count
    return count


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_positive_basic():
    assert count_positive([3, -1, 4, -1, 5]) == 3

def test_positive_none():
    assert count_positive([-2, -7, 0]) == 0

def test_positive_all():
    assert count_positive([1, 2, 3]) == 3

def test_positive_empty():
    assert count_positive([]) == 0

def test_short_basic():
    assert count_short(["hi", "cat", "elephant", "go"]) == 3

def test_short_all():
    assert count_short(["a", "be", "cup"]) == 3

def test_short_none():
    assert count_short(["long", "words", "only"]) == 1

def test_short_empty():
    assert count_short([]) == 0
