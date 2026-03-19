# 03_accumulate.py
# Named Loop Pattern: ACCUMULATE
#
# Walk the whole list. Combine each element into a running total.
# The total starts at an identity value (0 for addition, "" for strings).
# Return the total at the end.
#
# Count is a special case of Accumulate (adding 1 each time).
# Here you add the element itself.
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 03_accumulate.py -v


def total(lst):
    """Return the sum of all floats in lst."""
    result = 0
    for item in lst:
        pass  # add item to result
    return result


def join_with_dash(lst):
    """Return all strings joined with '-' between them.

    Example: ["a", "b", "c"] → "a-b-c"
    Hint: build up the string, then slice off the leading dash.
    """
    result = ""
    for item in lst:
        pass  # append a dash and the item to result
    return result[1:]  # remove the leading dash


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_total_basic():
    assert total([1.5, 2.5, 3.0]) == 7.0

def test_total_negatives():
    assert total([-1.0, 1.0, -2.0, 2.0]) == 0.0

def test_total_single():
    assert total([4.2]) == 4.2

def test_total_empty():
    assert total([]) == 0

def test_join_basic():
    assert join_with_dash(["a", "b", "c"]) == "a-b-c"

def test_join_words():
    assert join_with_dash(["hip", "hop"]) == "hip-hop"

def test_join_single():
    assert join_with_dash(["ok"]) == "ok"
