"""Test package for experimenting with setuptools_scm-based releases."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("release-test")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
