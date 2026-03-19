# 01_visit_all.py
# Named Loop Pattern: VISIT ALL
#
# The simplest loop pattern — do something to EVERY element.
# No skipping, no early exit. Walk the whole list, build a new one.
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 01_visit_all.py -v


def double_all(lst):
    """Return a new list where every integer is doubled."""
    result = []
    for item in lst:
        pass  # append the doubled item to result
    return result


def shout_all(lst):
    """Return a new list where every string is uppercased."""
    result = []
    for item in lst:
        pass  # append the uppercased item to result
    return result


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_double_basic():
    assert double_all([1, 2, 3]) == [2, 4, 6]

def test_double_negatives():
    assert double_all([-3, 0, 5]) == [-6, 0, 10]

def test_double_empty():
    assert double_all([]) == []

def test_double_single():
    assert double_all([7]) == [14]

def test_shout_basic():
    assert shout_all(["hi", "bye"]) == ["HI", "BYE"]

def test_shout_chars():
    assert shout_all(["a", "b", "c"]) == ["A", "B", "C"]

def test_shout_empty():
    assert shout_all([]) == []

def test_shout_already_upper():
    assert shout_all(["OK", "go"]) == ["OK", "GO"]
