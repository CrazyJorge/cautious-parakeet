# 05_find_best.py
# Named Loop Pattern: FIND BEST
#
# Walk the whole list. Track the best value seen so far.
# Each element either beats the current best or it doesn't.
#
# KEY DECISION: what do you initialise best to?
# Answer: the first element.  Not zero, not None.
# (Why not zero?  What if every element is negative?)
#
# No early exit — you must see every element to be sure.
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 05_find_best.py -v


def find_max(lst):
    """Return the largest integer in lst."""
    best = lst[0]
    for item in lst:
        pass  # if item beats best, update best
    return best


def find_min_char(lst):
    """Return the smallest single character in lst (by ASCII order).

    Reminder: 'A' < 'Z' < 'a' < 'z'
    """
    best = lst[0]
    for item in lst:
        pass  # if item beats best, update best
    return best


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_max_basic():
    assert find_max([3, 1, 4, 1, 5, 9, 2, 6]) == 9

def test_max_negatives():
    assert find_max([-5, -1, -8, -2]) == -1

def test_max_single():
    assert find_max([42]) == 42

def test_max_all_same():
    assert find_max([7, 7, 7]) == 7

def test_max_at_start():
    assert find_max([9, 1, 2, 3]) == 9

def test_min_char_basic():
    assert find_min_char(["f", "a", "m", "b", "z"]) == "a"

def test_min_char_upper():
    assert find_min_char(["z", "A", "m", "B"]) == "A"

def test_min_char_single():
    assert find_min_char(["q"]) == "q"

def test_min_char_same():
    assert find_min_char(["e", "e", "e"]) == "e"
