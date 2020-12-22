"""Test Task-Runner."""
from invoke import call, task

__version__ = '0.1.0'

@task
def check_pass(ctx, password=None, policy="strict"):
    """Check the specified password.

    :param password, str required
    :param policy, str optional
    """
    ctx.run("echo HELLO")
