# 08_check_any.py
# Named Loop Pattern: CHECK ANY
#
# Question: does AT LEAST ONE element satisfy a condition?
#
# Walk the list. The moment you find one element that PASSES,
# return True immediately.  One success answers the question.
#
# If you survive the whole loop without a hit, return False.
#
# Early exit on SUCCESS.  (Compare with Check All — early exit on failure.)
# Together, Check All and Check Any are the loop versions of
# Python's built-in all() and any().
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 08_check_any.py -v


def any_negative(lst):
    """Return True if at least one integer in lst is negative."""
    for item in lst:
        pass  # if item meets the condition, return True now
    return False


def any_upper(lst):
    """Return True if at least one string in lst is fully uppercase."""
    for word in lst:
        pass  # if word meets the condition, return True now
    return False


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_any_neg_yes():
    assert any_negative([3, -1, 4]) is True

def test_any_neg_no():
    assert any_negative([3, 1, 4]) is False

def test_any_neg_all():
    assert any_negative([-1, -2, -3]) is True

def test_any_neg_empty():
    assert any_negative([]) is False

def test_any_neg_single_yes():
    assert any_negative([-5]) is True

def test_any_neg_single_no():
    assert any_negative([5]) is False

def test_any_upper_yes():
    assert any_upper(["hi", "OK", "bye"]) is True

def test_any_upper_no():
    assert any_upper(["hi", "Ok", "bye"]) is False

def test_any_upper_empty():
    assert any_upper([]) is False

def test_any_upper_single():
    assert any_upper(["GO"]) is True
