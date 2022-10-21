=============================
pre-commit hooks django migrations
=============================

.. image:: https://badge.fury.io/py/pre-commit-dotenv-checker.svg/?style=flat-square
    :target: https://badge.fury.io/py/pre-commit-dotenv-checker

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://pre-commit-dotenv-checker.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/pre-commit-dotenv-checker/main?style=flat-square
    :target: https://coveralls.io/github/frankhood/pre-commit-dotenv-checker?branch=main
    :alt: Coverage Status

Hook for pre-commit and Django migrations

Documentation
-------------

The full documentation is at https://pre-commit-dotenv-checker.readthedocs.io.

Quickstart
----------

Use this hook in your `.pre-commit-config.yaml` like this:

.. code-block:: yaml

    repos:
    - repo: https://github.com/frankhood/pre-commit-dotenv-checker
        rev: {{tag name}}  
        hooks:
        - id: makemigrations-check-absent
            name: "Check for absent migrations"

Features
--------

* TODO

Running Tests
-------------


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
