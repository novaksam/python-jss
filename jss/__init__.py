#!/usr/bin/env python
"""
python-jss
Python wrapper for JSS API.

Copyright (C) 2014 Shea G Craig <shea.craig@da.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


from jss import *
from casper import Casper
from distribution_points import DistributionPoints
from exceptions import (
    JSSPrefsMissingFileError, JSSPrefsMissingKeyError, JSSGetError,
    JSSPutError, JSSPostError, JSSDeleteError, JSSMethodNotAllowedError,
    JSSUnsupportedSearchMethodError, JSSFileUploadParameterError,
    JSSUnsupportedFileType)

__version__ = "0.5.9"
