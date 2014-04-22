=============
Mr.Gutenberg
=============

is a buildout recipe which will install and setup `Sphinx <http://sphinx-doc.org/>`_ following the Documentation Guidelines of the Plone Foundation for your Project.
The aim of mr.gutenberg is to make documentation so painless as possible for
developers.

What it does:
-------------
mr.gutenberg will install Sphinx and will do the setup. You will end up with a
folder called ''docs'' in your buildout, this folder contains Sphinx and all
related files and config.
In addition you will find some boilerplate templates, which make it easier to
write documentation.
mr.gutenberg will create an index.rst which will be filled with base data out of
your setup.py (like the Author, Description and so on).

Options:
--------

Till we fetch these from setup.py we will have to configure some options in
your buildout.cfg.


    project = plone.app.welikedocs

    author = Sven

**This is pretty much WIP and not fully working yet !!!**
