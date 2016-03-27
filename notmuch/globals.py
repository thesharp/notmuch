"""
This file is part of notmuch.

Notmuch is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

Notmuch is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License
along with notmuch.  If not, see <http://www.gnu.org/licenses/>.

Copyright 2010 Sebastian Spaeth <Sebastian@SSpaeth.de>
"""

from ctypes import CDLL, Structure, POINTER
from os import uname

#-----------------------------------------------------------------------------
#package-global instance of the notmuch library
if uname()[0] = "Darwin":
    __LIB = "libnotmuch.4.dylib"
else:
    __LIB = "libnotmuch.so.4"

try:
    nmlib = CDLL(__LIB)
except:
    raise ImportError("Could not find shared 'notmuch' library: %s." % __LIB)

from .compat import Python3StringMixIn, encode_utf8 as _str

class Enum(object):
    """Provides ENUMS as "code=Enum(['a','b','c'])" where code.a=0 etc..."""
    def __init__(self, names):
        for number, name in enumerate(names):
            setattr(self, name, number)


class NotmuchDatabaseS(Structure):
    pass
NotmuchDatabaseP = POINTER(NotmuchDatabaseS)


class NotmuchQueryS(Structure):
    pass
NotmuchQueryP = POINTER(NotmuchQueryS)


class NotmuchThreadsS(Structure):
    pass
NotmuchThreadsP = POINTER(NotmuchThreadsS)


class NotmuchThreadS(Structure):
    pass
NotmuchThreadP = POINTER(NotmuchThreadS)


class NotmuchMessagesS(Structure):
    pass
NotmuchMessagesP = POINTER(NotmuchMessagesS)


class NotmuchMessageS(Structure):
    pass
NotmuchMessageP = POINTER(NotmuchMessageS)


class NotmuchTagsS(Structure):
    pass
NotmuchTagsP = POINTER(NotmuchTagsS)


class NotmuchDirectoryS(Structure):
    pass
NotmuchDirectoryP = POINTER(NotmuchDirectoryS)


class NotmuchFilenamesS(Structure):
    pass
NotmuchFilenamesP = POINTER(NotmuchFilenamesS)
