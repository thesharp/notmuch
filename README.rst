notmuch -- The python interface to notmuch.so
==============================================

About this particular repository
--------------------------------

This repository contains a patched bindings of notmuch version 0.15.2, which will work on Mac OS X. The sources are modified with this `patch <http://article.gmane.org/gmane.mail.notmuch.general/15419>`__ in mind, and the version of the library has been synchronized with the current notmuch from `homebrew <http://brew.sh>`__ (0.21).

Description
----------

This module makes the functionality of the notmuch library
(`http://notmuchmail.org`_) available to python. Successful import of
this modul depends on a libnotmuch.so|dll being available on the
user's system.

If you have downloaded the full source tarball, you can create the
documentation with sphinx installed, go to the docs directory and
"make html". A static version of the documentation is available at:

http://packages.python.org/notmuch/

The current source code is being hosted at
http://bitbucket.org/spaetz/cnotmuch which also provides an issue
tracker, and release downloads. This package is tracked by the python
package index repository at `http://pypi.python.org/pypi/notmuch`_ and can thus be installed on a user's computer easily via "sudo easy_install notmuch" (you will still need to install the notmuch shared library separately as it is not included in this package).

The original source has been provided by (c)Sebastian Spaeth, 2010.
All code is available under the GNU GPLv3+ (see docs/COPYING) unless specified otherwise.


INSTALLATION & DEINSTALL
------------------------

The notmuch python module is available on pypi.python.org. This means
you can do "easy_install notmuch" on your linux box and it will get
installed into:

/usr/local/lib/python2.x/dist-packages/

For uninstalling, you'll need to remove the "notmuch-0.4-py2.x.egg"
(or similar) directory and delete one entry in the "easy-install.pth"
file in that directory.

It needs to have a libnotmuch.so or libnotmuch.so.1 available in some
library folder or will raise an exception when loading.
"OSError: libnotmuch.so.1: cannot open shared object file: No such file or directory"


Usage
-----
For more examples of how to use the notmuch interface, have a look at the
notmuch "binary" and the generated documentation.

Example session:
>>>import notmuch
>>>db = notmuch.Database("/home/spaetz/mail")
db.get_path()
'/home/spaetz/mail'
>>>tags = db.get_all_tags()
>>>for tag in tags: 
>>>  print tag
inbox
...
maildir::draft
#---------------------------------------------

q = notmuch.Query(db,'from:Sebastian')
count = len(q.search_messages())
1300

#---------------------------------------------

>>>db = notmuch.Database("/home/spaetz/mailHAHA")
NotmuchError: Could not open the specified database

#---------------------------------------------

>>>tags = notmuch.Database("/home/spaetz/mail").get_all_tags()
>>>del(tags)


Building for a Debian package
------------------------------
dpkg-buildpackage -i"\.hg|\/build"


Changelog
---------
0.1   First public release
0.1.1 Fixed Database.create_query()
0.2.0 Implemented Thread() and Threads() methods
0.2.1 Implemented the remaining API methods, notably Directory() and Filenames()
0.2.2 Bug fixes
0.3.0 Incorporated in the notmuchmail.org git repository
