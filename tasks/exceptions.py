"""Provide Check Pass Exceptions."""


class ValidatorException(Exception):
    """Provide validator base."""


class InvalidParams(ValidatorException):
    """Provide exception for invalid parameters."""
