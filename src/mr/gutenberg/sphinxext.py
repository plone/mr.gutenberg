from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.compat import Directive
from sphinx.util.docstrings import prepare_docstring
from sphinx.util.nodes import nested_parse_with_titles

tpl_package_info_table = """\
+------------+----------------+
| title      | value          |
+============+================+
| replace    | replace        |
+------------+----------------+
"""


class BaseDirective(Directive):

    def _rest2node(self, rest, container=None):
        """ creates a docutils node from some rest-markup
        """
        vl = ViewList(prepare_docstring(rest))
        if container is None:
            node = nodes.container()
        else:
            node = container()
        nested_parse_with_titles(self.state, vl, node)
        return node


class InfoTableDirective(BaseDirective):
    """creates an table with information from setup.py
    """
    def run(self):
        """a table containing base package info

        returns a list of nodes (in this case one node)
        """
        dummy_value = {'foo': 'bar', 'willi': 'wonka'}

        table = self._rest2node(tpl_package_info_table)
        rows = table.children[0].children[0].children[3].children[0]
        rows[0].children = []
        rows[1].children = []

        for key, value in dummy_value.items():
            rows[0].append(nodes.paragraph(text=key))
            rows[1].append(nodes.paragraph(text=value))
        return [table]
