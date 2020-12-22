"""Validator Config."""

import os

__version__ = "0.1.0"

test_good = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "tests/good_passwords.txt"
    )
)
test_bad = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "tests/bad_passwords.txt"
    )
)
common_passwords = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "tests/common_passwords.txt"
    )
)
input_file = os.environ.get(
    "PASS_CHECK_FILE",
    test_good
)
bad_input_file = os.environ.get(
    "PASS_CHECK_BAD",
    test_bad
)
common_passwords_file = os.environ.get(
    "COMMON_CHECK_FILE",
    common_passwords
)
