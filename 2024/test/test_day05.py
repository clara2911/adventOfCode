from pathlib import Path
import logging
import day05
import pytest

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture
def test_updates():
    test_updates = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]
    yield test_updates


@pytest.fixture
def test_rules():
    test_rules = [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
            (53, 13),
        ]
    yield test_rules


def test_part1_example_middle_page_sum_of_correct_orderings_matches_puzzle_description():
    sum_middles = day05.get_solution_part1(input_path=Path("../input/day05/test_input.txt"))
    assert sum_middles == 143


def test_part2_example_middle_page_sum_of_incorrect_orderings_matches_puzzle_description():
    sum_middles = day05.get_solution_part2(input_path=Path("../input/day05/test_input.txt"))
    assert sum_middles == 123


def test_read_input(test_updates, test_rules):
    read_updates, read_rules = day05.read_input(Path("../input/day05/test_input.txt"))
    assert read_updates == test_updates
    assert read_rules == test_rules


def test_is_correctly_ordered(test_updates, test_rules):
    output = day05.get_update_validity_mask(updates=test_updates, rules=test_rules)
    expected_output = [True, True, True, False, False, False]
    assert (output == expected_output).all()


def test_sum_middles(test_updates):
    valid_updates = [
        [75, 47, 61, 53, 29],  # 61
        [97, 61, 53, 29, 13],  # 53
        [75, 29, 13],  # 29
    ]
    output = day05.sum_middle_pagenumbers(updates=valid_updates)
    expected_output = 143
    assert output == expected_output


def test_make_page_adhere_to_rules(test_updates, test_rules):
    invalid_update = [75, 97, 47, 61, 53]
    output = day05.make_page_adhere_to_rules(page_number=75, update=invalid_update, rules=test_rules)
    expected_output = [97, 75, 47, 61, 53]
    assert output == expected_output


