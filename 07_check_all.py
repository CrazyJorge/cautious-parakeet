# 07_check_all.py
# Named Loop Pattern: CHECK ALL
#
# Question: does EVERY element satisfy a condition?
#
# Walk the list. The moment you find one element that FAILS,
# return False immediately.  No need to check the rest —
# one failure is enough to answer "no, not all."
#
# If you survive the whole loop, return True.
#
# Early exit on FAILURE.  (Compare with Check Any — early exit on success.)
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 07_check_all.py -v


def all_positive(lst):
    """Return True if every integer in lst is greater than zero."""
    for item in lst:
        if item <= 0:
            return False
    return True


def all_short(lst):
    """Return True if every string in lst has length <= 3."""
    for word in lst:
        if len(word) > 3:
            return False
    return True


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_all_pos_yes():
    assert all_positive([1, 2, 3]) is True

def test_all_pos_no():
    assert all_positive([1, -2, 3]) is False

def test_all_pos_zero():
    assert all_positive([1, 0, 3]) is False

def test_all_pos_empty():
    assert all_positive([]) is True  # vacuous truth

def test_all_pos_single_yes():
    assert all_positive([5]) is True

def test_all_pos_single_no():
    assert all_positive([-1]) is False

def test_all_short_yes():
    assert all_short(["hi", "cat", "go"]) is True

def test_all_short_no():
    assert all_short(["hi", "tiger", "go"]) is False

def test_all_short_empty():
    assert all_short([]) is True

def test_all_short_exact():
    assert all_short(["abc", "de", "f"]) is True
