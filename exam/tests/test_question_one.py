"""Confirm the correctness of functions in question_one."""

import json

import pytest
import yaml

# ruff: noqa: PLR2004
from questions.question_one import (
    CoverageItem,
    calculate_coverage_score,
    compute_coverage_difference,
    compute_coverage_intersection,
    read_coverage_report_from_json,
    read_coverage_report_from_yaml,
)


@pytest.mark.question_one_part_a
def test_compute_coverage_difference():
    """Confirm correctness of question part."""
    item1 = CoverageItem(1, "line1", True)
    item2 = CoverageItem(2, "line2", True)
    item3 = CoverageItem(3, "line3", True)
    item4 = CoverageItem(4, "line4", True)
    item5 = CoverageItem(5, "line5", True)
    item6 = CoverageItem(6, "line6", True)
    item7 = CoverageItem(1, "line1", False)
    item8 = CoverageItem(2, "line2", False)
    item9 = CoverageItem(3, "line3", False)
    assert compute_coverage_intersection(
        [item1, item2, item3], [item1, item2, item3]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item4, item5, item6])
        == []
    ), "Failed on case with no common coverage"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item2, item3, item4]
    ) == [
        item2,
        item3,
    ], "Failed on case with partial overlap"
    assert compute_coverage_intersection(
        [item1, item2, item3], [item3, item2, item1]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_intersection([], []) == []
    ), "Failed on case with empty coverage reports"
    assert (
        compute_coverage_intersection([item1, item2, item3], [item7, item8, item9])
        == []
    ), "Failed on case with same ids but not covered"
    assert (
        compute_coverage_difference([item1, item2, item3], [item1, item2, item3]) == []
    ), "Failed on case with identical coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item4, item5, item6]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with no common coverage"
    assert compute_coverage_difference(
        [item1, item2, item3], [item2, item3, item4]
    ) == [item1], "Failed on case with partial overlap"
    assert (
        compute_coverage_difference([item1, item2, item3], [item3, item2, item1]) == []
    ), "Failed on case with identical coverage reports in different order"
    assert (
        compute_coverage_difference([], []) == []
    ), "Failed on case with empty coverage reports"
    assert compute_coverage_difference(
        [item1, item2, item3], [item7, item8, item9]
    ) == [
        item1,
        item2,
        item3,
    ], "Failed on case with same ids but different coverage status"


@pytest.mark.question_one_part_b
def test_compute_coverage_score():
    """Confirm correctness of question part."""
    # test with an empty list
    assert calculate_coverage_score([]) == 0.0, "Failed on empty list"
    # test with all items covered
    all_covered = [CoverageItem(1, "line1", True) for _ in range(5)]
    assert calculate_coverage_score(all_covered) == 1.0, "Failed on all items covered"
    # test with no items covered
    none_covered = [CoverageItem(1, "line1", False) for _ in range(5)]
    assert calculate_coverage_score(none_covered) == 0.0, "Failed on no items covered"
    # test with some items covered
    some_covered = [
        CoverageItem(1, "line1", True),
        CoverageItem(2, "line2", False),
        CoverageItem(3, "line3", True),
    ]
    assert (
        calculate_coverage_score(some_covered) == 2 / 3
    ), "Failed on some items covered"
    # test with one item covered
    one_covered = [CoverageItem(1, "line1", True)]
    assert calculate_coverage_score(one_covered) == 1.0, "Failed on one item covered"
    # test with one item not covered
    one_not_covered = [CoverageItem(1, "line1", False)]
    assert (
        calculate_coverage_score(one_not_covered) == 0.0
    ), "Failed on one item not covered"


@pytest.mark.question_one_part_c
def test_read_coverage_report_from_json(tmp_path):
    """Confirm correctness of question part."""
    # define the JSON content for the test
    coverage_data = [
        {"id": 1, "line": "int a = 0", "covered": True},
        {"id": 2, "line": "    pass", "covered": False},
    ]
    # create a temporary file and write the JSON content to it
    temp_file = tmp_path / "coverage_report.json"
    with temp_file.open("w") as f:
        json.dump(coverage_data, f)
    # read the coverage report from the temporary file
    coverage_report = read_coverage_report_from_json(str(temp_file))
    # assertions with diagnostic messages
    assert len(coverage_report) == 2, "Expected 2 coverage items, got {0}".format(
        len(coverage_report)
    )
    assert (
        coverage_report[0].id == 1
    ), "Expected id 1 for the first item, got {0}".format(coverage_report[0].id)
    assert (
        coverage_report[0].line == "int a = 0"
    ), "Expected line 'int a = 0' for the first item, got {0}".format(
        coverage_report[0].line
    )
    assert (
        coverage_report[0].covered is True
    ), "Expected covered True for the first item, got {0}".format(
        coverage_report[0].covered
    )
    assert (
        coverage_report[1].id == 2
    ), "Expected id 2 for the second item, got {0}".format(coverage_report[1].id)
    assert (
        coverage_report[1].line == "    pass"
    ), "Expected line '    pass' for the second item, got {0}".format(
        coverage_report[1].line
    )
    assert (
        coverage_report[1].covered is False
    ), "Expected covered False for the second item, got {0}".format(
        coverage_report[1].covered
    )


@pytest.mark.question_one_part_c
def test_read_coverage_report_from_empty_json(tmp_path):
    """Test reading an empty JSON file."""
    # create an empty JSON file
    temp_file = tmp_path / "empty_coverage_report.json"
    with temp_file.open("w") as f:
        json.dump([], f)
    # read the coverage report from the empty JSON file
    coverage_report = read_coverage_report_from_json(str(temp_file))
    # confirm that parsing works correctly
    # when there are no coverage items
    # specified in the JSON file
    assert len(coverage_report) == 0, "Expected 0 coverage items, got {0}".format(
        len(coverage_report)
    )


@pytest.mark.question_one_part_d
def test_read_coverage_report_from_yaml(tmp_path):
    """Confirm correctness of question part."""
    # define the YAML content for the test
    coverage_data = [
        {"id": 1, "line": "int a = 0", "covered": True},
        {"id": 2, "line": "    pass", "covered": False},
    ]
    # create a temporary file and write the YAML content to it
    temp_file = tmp_path / "coverage_report.yaml"
    with temp_file.open("w") as f:
        yaml.dump(coverage_data, f)
    # read the coverage report from the temporary file
    coverage_report = read_coverage_report_from_yaml(str(temp_file))
    # assertions with diagnostic messages
    assert len(coverage_report) == 2, "Expected 2 coverage items, got {0}".format(
        len(coverage_report)
    )
    assert (
        coverage_report[0].id == 1
    ), "Expected id 1 for the first item, got {0}".format(coverage_report[0].id)
    assert (
        coverage_report[0].line == "int a = 0"
    ), "Expected line 'int a = 0' for the first item, got {0}".format(
        coverage_report[0].line
    )
    assert (
        coverage_report[0].covered is True
    ), "Expected covered True for the first item, got {0}".format(
        coverage_report[0].covered
    )
    assert (
        coverage_report[1].id == 2
    ), "Expected id 2 for the second item, got {0}".format(coverage_report[1].id)
    assert (
        coverage_report[1].line == "    pass"
    ), "Expected line '    pass' for the second item, got {0}".format(
        coverage_report[1].line
    )
    assert (
        coverage_report[1].covered is False
    ), "Expected covered False for the second item, got {0}".format(
        coverage_report[1].covered
    )


@pytest.mark.question_one_part_d
def test_read_coverage_report_from_empty_yaml(tmp_path):
    """Test reading an empty YAML file."""
    # create an empty YAML file
    temp_file = tmp_path / "empty_coverage_report.yaml"
    with temp_file.open("w") as f:
        yaml.dump([], f)
    # read the coverage report from the empty YAML file
    coverage_report = read_coverage_report_from_yaml(str(temp_file))
    # assertions with diagnostic messages
    assert len(coverage_report) == 0, "Expected 0 coverage items, got {0}".format(
        len(coverage_report)
    )
