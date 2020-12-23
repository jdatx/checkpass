"""Test Task-Runner."""

import os

from invoke import task
from password_validation import PasswordPolicy

from . import config, exceptions

__version__ = '0.1.0'


class PasswordValidator(object):
    """Validates passwords based on rules."""

    @property
    def policy(self):
        """Return set policy."""
        return self._password_policy()

    def __init__(self, input_file: str, check_file: str):
        """Initialize password validator."""
        self.input_file = input_file
        self.check_file = check_file

        if self.check_files():
            raise exceptions.InvalidParams("Invalid files")

    def check_files(self):
        """Check to make sure parameters are present."""
        def file_check():
            for file in [self.input_file, self.check_file]:
                if not os.path.exists(file):
                    yield file
                elif not os.path.isfile(file):
                    yield file
                elif os.stat(file).st_size == 0:
                    yield file
                else:
                    continue
        return [f for f in file_check()]

    def _password_policy(self, policy_type='strict'):
        """Set password policy used.

        :param policy_type: str, optional
        """
        def get_forbidden():
            with open(self.check_file) as fp:
                for line in fp.readlines():
                    yield line.strip("\n")
        return PasswordPolicy(
            min_length=8,
            forbidden_words=[
                w for w in get_forbidden()
            ]
        )

    def policy_check(self):
        """Check passwords from input file against policy."""
        def yeild_bad():
            with open(self.input_file) as fp:
                for line in fp.readlines():
                    tp = line.strip("\n")
                    if not self.policy.validate(tp):
                        yield tp
        return [p for p in yeild_bad()]


@task
def check_pass(ctx, file=config.input_file):
    """Check the specified password.

    :param file, str optional
    """
    pv = PasswordValidator(
        input_file=file,
        check_file=config.common_passwords_file
    )
    results = pv.policy_check()
    print(results)
