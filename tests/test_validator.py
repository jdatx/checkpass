import unittest

from tasks import config, validator

pos_test_validator = validator.PasswordValidator(
    input_file=config.input_file,
    check_file=config.common_passwords_file
)
neg_test_validator = validator.PasswordValidator(
    input_file=config.bad_input_file,
    check_file=config.common_passwords_file
)


class TestValidator(unittest.TestCase):
    """Test Validator."""

    def test_check_files(self):
        """Test check files."""
        ptr = pos_test_validator.check_files()
        ntr = neg_test_validator.check_files()
        assert not ptr
        assert not ntr

    def test_policy_check(self):
        """Test policy check."""
        ptr = pos_test_validator.policy_check()
        ntr = neg_test_validator.policy_check()
        assert not ptr
        assert ntr
