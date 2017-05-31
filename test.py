import pytest
from tslsr import utils as tslsr_utils


def test_is_contains_rectangle():
    rect1 = (0, 0, 10, 20)
    rect2 = (5, 10, 2, 2)
    assert tslsr_utils.is_contains_rectangle(rect1, rect2) == True
    rect2 = (5, 10, 2, 20)
    assert tslsr_utils.is_contains_rectangle(rect1, rect2) == False
    assert tslsr_utils.is_contains_rectangle(rect1, rect1) == False
