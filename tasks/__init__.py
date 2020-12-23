# -*- coding: utf-8 -*-
"""Check Pass."""

__title__ = """Check Pass.."""
__version__ = "0.1.0"

__all__ = []

import logging

from invoke import Collection

from . import validator

logging.getLogger(__name__).addHandler(logging.NullHandler())

ns = Collection(
    validator
)
