# -*- coding: utf-8 -*-
from zc.recipe.egg import Scripts
import os
import re

TPL_DIR = os.path.join(os.path.dirname(__file__), 'templates')
TPLS = [
    ('conf.py', 'sources',),
    ('index.rst', 'sources'),
    ('Makefile', ''),
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
        sourcesdir = os.path.join(self.docsdir, 'sources')
        if not os.path.exists(self.docsdir):
            os.mkdir(self.docsdir)
        if not os.path.exists(sourcesdir):
            os.mkdir(sourcesdir)

        # templates kopieren (conf, rst)
        for tplname, tplsubdir in TPLS:
            target = os.path.join(self.docsdir, tplsubdir, tplname)
            with open(os.path.join(TPL_DIR, tplname)) as tpl_file:
                tpl = tpl_file.read()
            tpl = self._render(tpl)
            with open(target, 'w') as target_file:
                target_file.write(tpl)

        # sphinx installieren
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
