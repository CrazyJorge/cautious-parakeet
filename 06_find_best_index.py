# 06_find_best_index.py
# Named Loop Pattern: FIND BEST INDEX
#
# Same as Find Best — but you need WHERE the best value is,
# not just what it is.
#
# Use enumerate(lst) to get (index, value) pairs.
# Track the best INDEX.  To compare, look up lst[best_idx].
#
# This is the inner loop of SELECTION SORT.
# Once you can find the index of the smallest element,
# you're one swap away from sorting.
#
# Your job: fill in the loop body so every test passes.
# Run with:  pytest 06_find_best_index.py -v


def max_index(lst):
    """Return the index of the largest integer in lst."""
    best_idx = 0
    for idx, item in enumerate(lst):
        pass  # if item beats lst[best_idx], update best_idx
    return best_idx


def min_index(lst):
    """Return the index of the smallest string in lst."""
    best_idx = 0
    for idx, item in enumerate(lst):
        pass  # if item beats lst[best_idx], update best_idx
    return best_idx


# ── Tests ──────────────────────────────────────────────────────────────────────


def test_max_idx_basic():
    assert max_index([3, 1, 9, 2, 6]) == 2

def test_max_idx_at_start():
    assert max_index([9, 1, 2, 3]) == 0

def test_max_idx_at_end():
    assert max_index([1, 2, 3, 9]) == 3

def test_max_idx_negatives():
    assert max_index([-5, -1, -8, -2]) == 1

def test_max_idx_single():
    assert max_index([4]) == 0

def test_min_idx_basic():
    assert min_index(["fox", "ant", "mug", "bat"]) == 1

def test_min_idx_at_start():
    assert min_index(["ant", "mug", "zoo"]) == 0

def test_min_idx_at_end():
    assert min_index(["mug", "zoo", "ant"]) == 2

def test_min_idx_single():
    assert min_index(["q"]) == 0

def test_min_idx_caps():
    assert min_index(["zoo", "Ant", "mug"]) == 1
