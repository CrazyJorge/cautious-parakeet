# loop_patterns_3.py
# O(n) Loop Patterns — Find Best (value and index)
#
# Same rules: explicit for loop, no built-ins that do the whole job.
# Tests use max() and min() as the answer key.


# ── Pattern 6: Find Biggest ─────────────────────────────────────────────────
#
# Track the best value seen so far.
# Start with the first element — not zero, not None.
# (Why not zero? What if every element is negative?)
#
# Integers.

def find_big(lst):
    """Return the largest value in lst."""
    best = lst[0]
    for item in lst:
        pass  # if item beats best, update best
    return best


# ── Pattern 7: Find Smallest ────────────────────────────────────────────────
#
# Same structure as Find Biggest — only the comparison flips.
# Recognizing that is the point.
#
# Single ASCII characters — min/max on chars uses ASCII order.
# 'A' < 'Z' < 'a' < 'z'  (uppercase comes before lowercase)

def find_small(lst):
    """Return the smallest character in lst."""
    best = lst[0]
    for item in lst:
        pass  # if item beats best, update best
    return best


# ── Pattern 8: Find Biggest Index ───────────────────────────────────────────
#
# Sometimes we need WHERE the best value is, not just what it is.
# enumerate(lst) gives us (index, value) pairs on every iteration.
#
# Track the best index, not the best value.
# To check if a new item is better, compare values — but store the index.
#
# Integers.

def find_big_idx(lst):
    """Return the index of the largest value in lst."""
    best_idx = 0
    for idx, item in enumerate(lst):
        pass  # if item beats lst[best_idx], update best_idx
    return best_idx


# ── Pattern 9: Find Smallest Index ──────────────────────────────────────────
#
# Same structure as Find Biggest Index — comparison flips.
# This pattern is the inner loop of selection sort.
#
# Single ASCII characters.

def find_small_idx(lst):
    """Return the index of the smallest character in lst."""
    best_idx = 0
    for idx, item in enumerate(lst):
        pass  # if item beats lst[best_idx], update best_idx
    return best_idx


# ── Tests ────────────────────────────────────────────────────────────────────
# Run with:  pytest loop_patterns_3.py -v


# -- find_big -----------------------------------------------------------------

def test_big_basic():
    lst = [3, 1, 4, 1, 5, 9, 2, 6]
    assert find_big(lst) == max(lst)

def test_big_negatives():
    lst = [-5, -1, -8, -2]
    assert find_big(lst) == max(lst)

def test_big_single():
    lst = [42]
    assert find_big(lst) == max(lst)

def test_big_all_same():
    lst = [7, 7, 7]
    assert find_big(lst) == max(lst)


# -- find_small ---------------------------------------------------------------

def test_small_basic():
    lst = ['f', 'a', 'm', 'b', 'z']
    assert find_small(lst) == min(lst)

def test_small_case():
    # uppercase sorts before lowercase in ASCII
    lst = ['z', 'A', 'm', 'B']
    assert find_small(lst) == min(lst)

def test_small_single():
    lst = ['q']
    assert find_small(lst) == min(lst)

def test_small_all_same():
    lst = ['e', 'e', 'e']
    assert find_small(lst) == min(lst)


# -- find_big_idx -------------------------------------------------------------

def test_big_idx_basic():
    lst = [3, 1, 9, 2, 6]
    assert find_big_idx(lst) == lst.index(max(lst))

def test_big_idx_at_start():
    lst = [9, 1, 2, 3]
    assert find_big_idx(lst) == lst.index(max(lst))

def test_big_idx_at_end():
    lst = [1, 2, 3, 9]
    assert find_big_idx(lst) == lst.index(max(lst))

def test_big_idx_negatives():
    lst = [-5, -1, -8, -2]
    assert find_big_idx(lst) == lst.index(max(lst))


# -- find_small_idx -----------------------------------------------------------

def test_small_idx_basic():
    lst = ['f', 'a', 'm', 'b', 'z']
    assert find_small_idx(lst) == lst.index(min(lst))

def test_small_idx_at_start():
    lst = ['a', 'm', 'z', 'f']
    assert find_small_idx(lst) == lst.index(min(lst))

def test_small_idx_at_end():
    lst = ['m', 'z', 'f', 'a']
    assert find_small_idx(lst) == lst.index(min(lst))

def test_small_idx_case():
    lst = ['z', 'A', 'm', 'B']
    assert find_small_idx(lst) == lst.index(min(lst))
