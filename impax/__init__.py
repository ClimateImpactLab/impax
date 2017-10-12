# -*- coding: utf-8 -*-

"""Top-level package for impax."""

from __future__ import absolute_import
from csvv import get_gammas
from mins import minimize_polynomial
from impax import Impact, construct_covars, construct_weather

__author__ = """Justin Simcock"""
__email__ = 'jsimcock@rhg.com'
__version__ = '0.1.0'


_module_imports = (
    get_gammas,
    minimize_polynomial,
    Impact,
    construct_weather,
    construct_covars,

)

__all__ = list(map(lambda x: x.__name__, _module_imports))