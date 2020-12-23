# Welcome to Check Pass

A cli utility for checking passwords against specified requirements.

## Commands

* `invoke checkpass --password="" --options=""` - Check a password.

## Dev, QA and Test
Setup.
```bash
~$ pip install --user pipenv
~$ pipenv shell
~$ (checkpass) $ pipenv install --dev
```
QA.
```bash
# Doc lint
~$ pydocstyle .
# Format
~$ isort --atomic **/*.py
~$ autopep8 **/*.py --max-line-length=80 --in-place
# Lint
~$ flake8
~$ yamllint -f standard
```
Test.
```bash
~$ pytest --capture='tee-sys'
~$ pytest --cov=. ./tests/
```