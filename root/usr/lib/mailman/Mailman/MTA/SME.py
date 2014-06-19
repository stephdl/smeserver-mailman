# Copyright (C) 2001,2002 by the Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

"""Creation/deletion hooks for the SME and Q-Mail
"""

import os
import time
import errno
import pwd
from stat import *

from Mailman import mm_cfg
from Mailman import Utils
from Mailman import LockFile
from Mailman.i18n import _
from Mailman.MTA.Utils import makealiases
from Mailman.Logging.Syslog import syslog



def create(mlist, cgi=0, nolock=0):
    listname = mlist.internal_name()
    msg = 'command failed: %s (status: %s, %s)'
    acmd = '/usr/lib/mailman/bin/smelist addlist ' + listname
    status = (os.system(acmd) >> 8) & 0xff
    if status:
        errstr = os.strerror(status)
        syslog('error', msg, acmd, status, errstr)
        raise RuntimeError, msg % (acmd, status, errstr)



def remove(mlist, cgi=0):
    listname = mlist.internal_name()
    msg = 'command failed: %s (status: %s, %s)'
    acmd = '/usr/lib/mailman/bin/smelist rmlist ' + listname
    status = (os.system(acmd) >> 8) & 0xff
    if status:
        errstr = os.strerror(status)
        syslog('error', msg, acmd, status, errstr)
        raise RuntimeError, msg % (acmd, status, errstr)
