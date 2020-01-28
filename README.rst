Intro
=====

This is my take on a python package development template. It includes a preconfigured
toolchain for creating, testing and publishing Python projects.

The tech stack:
    * `Poetry <https://python-poetry.org/docs/>`_ for dependency, virtual environment
    and build management.
    * `Tox <https://tox.readthedocs.io/en/latest/>`_ for generic automatization and
    multi version python testing.
    * `Pytest <https://docs.pytest.org/en/latest/>`_ for running unit tests and creating
    coverage reports.
    Linting and formatting stack:
        * `Black <https://black.readthedocs.io/en/stable/>`_
        * `Flake8 <https://flake8.pycqa.org/en/latest/>`_
        * `Isort <https://timothycrosley.github.io/isort/>`_
    * `Pre-commit <https://pre-commit.com/>`_ to run linting in a pre-commit hook

All these tools come with some (for me) sane default configurations, but feel free to
modify them.
