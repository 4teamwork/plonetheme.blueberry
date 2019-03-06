plonetheme.blueberry
=====================

An `ftw.theming`_ based Plone 4 and Plone 5.1 theme.


Note on Plone 5.1.x
-------------------

Currently there is no upgrade path tested for this package. Consider a reinstall if you upgrade from Plone 4.3.x to Plone 5.1.x.
A working upgrade path will be added later.


Installation
------------

Add ``plonetheme.blueberry`` to your buildout configuration

::

    [instance]
    eggs +=
        plonetheme.blueberry

or as dependency to the ``setup.py`` of your policy package.


Styles
------

There are multiple styles in this theme, which can be selected by
installing the corresponding Generic Setup profile.

- **Blueberry Standard Style**: The target audience of this style are
  municipalities and other government websites.

- **Blueberry Marketing Style**: The target audience of this style are
  product presentation and marketing websites.



Links
-----

- Github project repository: https://github.com/4teamwork/plonetheme.blueberry
- Issue tracker: https://github.com/4teamwork/plonetheme.blueberry/issues
- Continuous integration: https://jenkins.4teamwork.ch/search?q=plonetheme.blueberry



Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``plonetheme.blueberry`` is licensed under GNU General Public License, version 2.


.. _ftw.theming: https://github.com/4teamwork/ftw.theming
