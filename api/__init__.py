# -*- coding: utf-8 -*-

"""
Noogal Python API Wrapper
~~~~~~~~~~~~~~~~~~~~~~
A wrapper for the noogalapp.com API.
:copyright: (c) 2019 noogalapp.com
:license: GPLv3, see LICENSE for more details.
"""

__title__ = 'noogal api'
__author__ = 'Francis Taylor'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2019 Noogal'
__version__ = '0.1.0-alpha'
__status__ = "Development"

from collections import namedtuple

# from .client import Client
from .errors import *
# from .http import HTTPClient

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel='alpha', serial=0)
