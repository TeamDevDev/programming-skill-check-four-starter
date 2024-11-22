"""Question One: Programming Skill Check."""

# TODO: The imports in the following source code block may no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

import json
import yaml
from typing import List


# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> This may has functions that may be seeded with defects; this means
# that you will have to improve various aspects of this code to ensure
# that it passes the various tests and checks.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml
# file in this GitHub repository for the configuration and name of each tool
# used to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Implement the following function(s) that perform an analysis of the test
# coverage data from more than one run of a test coverage monitoring tool.

# Function description:
# The function compute_coverage_intersection should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage intersection
#     between the two coverage reports
# --> The coverage intersection is the set of CoverageItem objects that
#     have the same id and are covered in both coverage reports

# Function description:
# The function compute_coverage_difference should:
# --> Take as input two lists of CoverageItem objects that represent the
#     coverage reports for a specific test run
# --> Return a list of CoverageItem objects that represent the coverage difference
#     between the two coverage reports
# --> The coverage difference is the set of CoverageItem objects that
#     are present in the first coverage report but not in the second
#     coverage report, based on the id and covered status

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.

# TODO: You do not need to modify any of the source code in the CoverageItem
# class. If you modify the source code the CoverageItem class it is likely
# that some of the tests for the required functions will not pass.


class CoverageItem:
    """A class to represent a coverage item."""

    def __init__(self, id: int, line: str, covered: bool):
        """Initialize the coverage item with the provided values."""
        self.id = id
        self.line = line
        self.covered = covered

    def __repr__(self):
        """Return a string representation of the coverage item."""
        return f"CoverageItem(id={self.id}, line='{self.line}', covered={self.covered})"

    def __str__(self):
        """Return a string representation of the coverage item."""
        return self.__repr__()


def compute_coverage_intersection(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage intersection between two coverage reports."""
    # initialize the coverage intersection to be an empty list
    coverage_intersection = []
    # return the coverage intersection
    return coverage_intersection


def compute_coverage_difference(
    coverage_report_one: List[CoverageItem], coverage_report_two: List[CoverageItem]
) -> List[CoverageItem]:
    """Compute the coverage difference between two coverage reports."""
    # initialize the coverage difference to be an empty list
    coverage_difference = []
    # return the coverage difference
    return coverage_difference


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function calculate_coverage_score should:
# --> Take as input a list of CoverageItem objects that represent the coverage
#     report for a specific test run
# --> Return a float that represents the coverage score, which is defined
#     as the number of covered lines divided by the total number of items
#     in the coverage report
# --> If the coverage report is empty, the function should return 0.0 to
#     indicate that no items were covered when the tests were run

# TODO: These functions may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations so that the
# function and any code that uses it passes the type checker.

# TODO: These functions may not have a docstring and thus it may not adhere to
# industry best practices for Python source code. You may need to add a
# docstring so that this function is correctly documented by an software
# engineer using it.


def calculate_coverage_score(coverage_items: List[CoverageItem]) -> float:
    """Calculate the coverage score from a list of CoverageItem instances."""
    return 0.0


# }}}

# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function read_coverage_report_from_json should:
# --> Take as input a file path as a string
# --> Return a list of CoverageItem objects that represent the coverage
#     report for a specific test run
# --> The coverage report is represented as a JSON file that contains a list
#     of JSON objects that each represent an instance of the CoverageItem class
# --> It should be able to parse the JSON file and convert it into a list of
#     CoverageItem objects that could be input to a function like
#     calculate_coverage_score that you implemented in part (b)

# Here is an example of a JSON file that this function could parse:

# [
#     {"id": 1, "line": "def foo():", "covered": true},
#     {"id": 2, "line": "    x = 1", "covered": true},
#     {"id": 3, "line": "    if x > 0:", "covered": false},
#     {"id": 4, "line": "        print('Positive')", "covered": false},
#     {"id": 5, "line": "    else:", "covered": true},
#     {"id": 6, "line": "        print('Non-positive')", "covered": true},
#     {"id": 7, "line": "def bar(y):", "covered": true},
#     {"id": 8, "line": "    return y * 2", "covered": false},
#     {"id": 9, "line": "# End of file", "covered": true}
# ]

# Please note that this is not the actual JSON file that is used to test your
# implementation of this function. Importantly, your implementation of
# read_coverage_report_from_json should be able to handle any JSON file
# that encodes the coverage of a program in the aforementioned format.

# You could image that this file was produced by a test coverage monitoring
# tool and then saved to the disk in a file called coverage.json.

# TODO: Your implementation of this function should not modify the existing
# implementation of the CoverageItem class.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def read_coverage_report_from_json(file_path: str) -> List[CoverageItem]:
    """Read and parse a JSON file to create a list of CoverageItem objects."""
    coverage_report = []
    return coverage_report


# }}}

# Part (d) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function read_coverage_report_from_yaml should:
# --> Take as input a file path as a string
# --> Return a list of CoverageItem objects that represent the coverage
#     report for a specific test run
# --> The coverage report is represented as a YAML file that contains a list
#     of YAML objects that each represent an instance of the CoverageItem class
# --> It should be able to parse the YAML file and convert it into a list of
#     CoverageItem objects that could be input to a function like
#     calculate_coverage_score that you implemented in part (b)
# --> Importantly, it must use the YAML-parsing functions that are
#     provided by the PyYAML library through the yaml module. To learn
#     more about this module you can reference the following web site:
#     https://github.com/yaml/pyyaml

# Here is an example of a YAML file that this function could parse:

# - id: 1
#   line: "def foo():"
#   covered: true
# - id: 2
#   line: "    x = 1"
#   covered: true
# - id: 3
#   line: "    if x > 0:"
#   covered: false
# - id: 4
#   line: "        print('Positive')"
#   covered: false
# - id: 5
#   line: "    else:"
#   covered: true
# - id: 6
#   line: "        print('Non-positive')"
#   covered: true
# - id: 7
#   line: "def bar(y):"
#   covered: true
# - id: 8
#   line: "    return y * 2"
#   covered: false
# - id: 9
#   line: "# End of file"
#   covered: true

# Please note that this is not the actual YAML file that is used to test your
# implementation of this function. Importantly, your implementation of
# read_coverage_report_from_yaml should be able to handle any YAML file
# that encodes the coverage of a program in the aforementioned format.

# You could imagine that this file was produced by a test coverage monitoring
# tool and then saved to the disk in a file called coverage.yaml.

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an software engineer using it.


def read_coverage_report_from_yaml(file_path: str) -> List[CoverageItem]:
    """Read and parse a YAML file to create a list of CoverageItem objects."""
    coverage_report = []
    return coverage_report


# }}}
