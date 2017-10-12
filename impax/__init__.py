# -*- coding: utf-8 -*-

"""Top-level package for impax."""

from __future__ import absolute_import
from mins import minimize_polynomial

__author__ = """Justin Simcock"""
__email__ = 'jsimcock@rhg.com'
__version__ = '0.1.0'


_module_imports = (
    minimize_polynomial,
)

__all__ = list(map(lambda x: x.__name__, _module_imports))