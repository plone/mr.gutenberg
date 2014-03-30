# -*- coding: utf-8 -*-
from zc.recipe.egg import Scripts
import os
import re

TPL_DIR = os.path.join(os.path.dirname(__file__), 'templates')
TPLS = [
    # filename, subpath, override
    ('conf.py', '', True),
    ('index.rst', 'source', False),
    ('Makefile', '', True),
]


class Recipe(object):

    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.buildout = buildout
        self.buildout_base = buildout['buildout']['directory']

        # eggs sphinx shall have available
        self.package = options.get('package')
        self.eggs = options.get('eggs', '')
        self.docsdir = options.get(
            'docs-directory',
            os.path.join(self.buildout_base, 'docs')
        )

    def install(self):
        """creates the initial structure for a addon documentation
        """
        # directory structure
        sourcesdir = os.path.join(self.docsdir, 'source')
        if not os.path.exists(self.docsdir):
            os.mkdir(self.docsdir)
        if not os.path.exists(sourcesdir):
            os.mkdir(sourcesdir)

        # create directory 'source/_images'
        sourceimagedir = os.path.join(self.docsdir, 'source','_images')
        if not os.path.exists(sourceimagedir):
            os.mkdir(sourceimagedir)

        # create directory '_static_'
        sourcestaticdir = os.path.join(self.docsdir, 'source','_static')
        if not os.path.exists(sourcestaticdir):
            os.mkdir(sourcestaticdir)

        # copy templates (conf, rst)
        for tplname, tplsubdir, override in TPLS:
            target = os.path.join(self.docsdir, tplsubdir, tplname)
            if not override and os.path.exists(target):
                continue
            with open(os.path.join(TPL_DIR, tplname)) as tpl_file:
                tpl = tpl_file.read()
            tpl = self._render(tpl)
            with open(target, 'w') as target_file:
                target_file.write(tpl)

        # install sphinx
        options = {'eggs': self.eggs + '\nSphinx'}
        scripts = Scripts(self.buildout, self.name, options)
        scripts.install()
        # install script for make docs in bin-directory
        return []

    def update(self):
        """checks if structure is already there, if not, create
        """
        return self.install()

    def _render(self, tpl):
        # stolen from collective.recipe.template
        template = re.sub(
            r"\$\{([^:]+?)\}", r"${%s:\1}" % self.name,
            tpl
        )
        return self.options._sub(template, [])
